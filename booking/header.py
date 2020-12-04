from booking.base_page import BasePage
from booking.locators import HeaderLocators


class Header(BasePage):
    """
    Реализации паттерна PageObject.
    Класс представляет собой Header страницы
    """

    def open_currency(self) -> None:
        """
        Открыть таблицу валют в которых показывать стоимость
        """
        self.find_element(HeaderLocators.CURRENCY_BUTTON).click()

    def click_to_RUB(self) -> None:
        """
        Выбрать Рубль как валюту в которой показывать стоимость
        """
        self.open_currency()
        self.find_element(HeaderLocators.SELECT_RUB_CURRENCY).click()

    def open_language(self) -> None:
        """
        Открыть таблицу языков
        """
        self.find_element(HeaderLocators.LANGUAGE_BUTTON).click()

    def click_to_language(self, abbreviation: str = 'ru') -> None:
        """
        Выбрать язык сайта
        :param abbreviation: абревиатура языка (по умолчанию: русский)
        """
        self.open_language()
        self.find_element(HeaderLocators.SELECT_COUNTRY_LANGUAGE(abbreviation)).click()
