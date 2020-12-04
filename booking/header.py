from booking.base_page import BasePage
from booking.locators import HeaderLocators


class Header(BasePage):
    def open_currency(self):
        self.find_element(HeaderLocators.CURRENCY_BUTTON).click()

    def click_to_RUB(self):
        self.find_element(HeaderLocators.SELECT_RUB_CURRENCY).click()

    def open_language(self):
        self.find_element(HeaderLocators.LANGUAGE_BUTTON).click()

    def click_to_language(self, abbreviation: str = 'ru'):
        self.find_element(HeaderLocators.SELECT_COUNTRY_LANGUAGE(abbreviation)).click()
