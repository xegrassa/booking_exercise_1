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

    def get_months(self):
        months = self.find_elements(MainPageLocators.MONTHS_CALENDAR)
        return [month.text for month in months]