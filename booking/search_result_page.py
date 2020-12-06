from typing import List

from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

from booking.base_page import BasePage
from booking.locators import SearchResultPageLocators


class SearchResultPage(BasePage):
    """
    Реализации паттерна PageObject.
    Класс представляет собой страницу с результатами поиска

    :atribute: filters - фильтры которые доступны
    :atribute: hotels - отели которые попадают под критерии фильтров
    """
    filters: List[WebElement] = None
    hotels: List[WebElement] = None
    cities: WebElement = None

    def select_cities(self, select_count: int = 20) -> None:
        """
        Выбирает в фильтре о городах первые 20 штук
        """
        self._get_cities()
        elements = self.cities.find_elements(*SearchResultPageLocators.CITY)
        for element in elements[:select_count]:
            try:
                self.visibility_of(element).click()
            except ElementNotInteractableException:
                print(element.text.split()[0], 'Был недоступен и нажали его скриптом JS')
                self.driver.execute_script("arguments[0].click();", element)

    def select_filter(self, needed_filter: str) -> bool:
        """
        На странице выбирает фильтр
        :param needed_filter: фильтр который надо найти и включить
        :return: None
        """
        self._get_filters()
        for filter_element in self.filters:
            if needed_filter in filter_element.text:
                filter_element.click()
                print(f'Фильтр: {needed_filter} включен')
                return True
        print(f'Фильтр: {needed_filter} не найден')
        return False

    def select_filters(self, filters_name: List[str]) -> None:
        """
        На странице выбирает фильтры
        :param filters_name: фильтры которые надо найти и включить
        :return: None
        """
        for filter_name in filters_name:
            if self.select_filter(filter_name):
                self.wait_spinner()

    def print_info_about_hotel(self, count_hotel: int = 10) -> None:
        """
        Выводит информацию об отелях
        :param count_hotel: кол-во отелей о которых выведется информация
        """
        self._get_hotels()
        for hotel in self.hotels[:count_hotel]:
            print(hotel.find_element(*SearchResultPageLocators.HOTEL_NAME).text)
            print(hotel.find_element(*SearchResultPageLocators.HOTEL_PRICE).text)
            try:
                print(hotel.find_element(*SearchResultPageLocators.HOTEL_SCORE).text)
            except NoSuchElementException:
                print("У Отеля нет оценки (недавно добавленный)")
            print('----------------------')

    def wait_spinner(self) -> None:
        """
        Ожидание конца спинера, при выборе фильтров
        """
        self.find_element(SearchResultPageLocators.SPINER)
        self.is_not_presence(SearchResultPageLocators.SPINER)

    def _get_cities(self) -> None:
        """
        Находит элемент с Городами и записывает в атрибут класса
        """
        self.find_element(SearchResultPageLocators.MORE_BUTTON).click()
        self.cities = self.find_element(SearchResultPageLocators.CITIES)

    def _get_filters(self) -> None:
        """
        Добавляет в атрибут обьекта фильтры доступные на странице
        """
        self.filters = self.find_elements(SearchResultPageLocators.FILTERS)

    def _get_hotels(self) -> None:
        """
        Добавляет в атрибут обьекта отели доступные на странице
        """
        self.hotels = self.find_elements(SearchResultPageLocators.HOTELS)
