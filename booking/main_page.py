import datetime

from selenium.common.exceptions import TimeoutException

from booking.base_page import BasePage
from booking.locators import MainPageLocators


class MainPage(BasePage):
    def open_currency(self):
        self.find_element(MainPageLocators.CURRENCY_BUTTON).click()

    def click_to_RUB(self):
        self.find_element(MainPageLocators.SELECT_RUB_CURRENCY).click()

    def open_language(self):
        self.find_element(MainPageLocators.LANGUAGE_BUTTON).click()

    def click_to_language(self, abbreviation: str = 'ru'):
        self.find_element(MainPageLocators.SELECT_COUNTRY_LANGUAGE(abbreviation)).click()

    def open_calendar(self):
        self.find_element(MainPageLocators.CALENDAR_BUTTON).click()

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
