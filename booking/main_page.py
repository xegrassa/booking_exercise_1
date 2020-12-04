import datetime

from selenium.common.exceptions import TimeoutException

from booking.base_page import BasePage
from booking.header import Header
from booking.locators import MainPageLocators
from booking.search_result_page import SearchResultPage


class MainPage(BasePage, Header):
    def open_calendar(self):
        self.find_element(MainPageLocators.CALENDAR_BUTTON).click()

    def open_guest_menu(self):
        self.find_element(MainPageLocators.GUEST_MENU).click()

    def input_destination(self, destination: str):
        self.find_element(MainPageLocators.DESTINATION_FIELD).send_keys(destination)

    def click_check_price(self):
        self.find_element(MainPageLocators.CHECK_PRICE_BUTTON).click()
        return SearchResultPage(self.driver)

    def select_date(self, date: str):
        certain_date = datetime.date.fromisoformat(date)
        locator = MainPageLocators.SELECT_CERTAIN_DATE(str(certain_date))
        while True:
            try:
                self.find_element(locator).click()
                break
            except TimeoutException:
                self._click_next_month()

    def _click_next_month(self):
        self.find_element(MainPageLocators.NEXT_MONTH_BUTTON).click()

    def select_guest(self, need_guest: int):
        while True:
            if need_guest == self._get_guest_count():
                break
            if need_guest > self._get_guest_count():
                self._add_guest()
            else:
                self._decrease_guest()

    def _decrease_guest(self):
        self.find_element(MainPageLocators.DECREASE_GUEST_BUTTON).click()

    def _add_guest(self):
        self.find_element(MainPageLocators.ADD_GUEST_BUTTON).click()

    def _get_guest_count(self):
        return int(self.find_element(MainPageLocators.GUEST_COUNT).text)
