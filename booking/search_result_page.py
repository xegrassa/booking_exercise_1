from time import sleep
from typing import List

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

    def select_filters(self, needed_filters: List[str]) -> None:
        """
        На странице выбирает фильтры
        :param needed_filters: фильтры которые надо найти и включить
        :return: None
        """
        for filter in needed_filters:
            self.select_filter(filter)
            sleep(5)

    def select_filter(self, needed_filter: str) -> None:
        """
        На странице выбирает фильтр
        :param needed_filter: фильтр который надо найти и включить
        :return: None
        """
        self._get_filters()
        for filter in self.filters:
            if needed_filter in filter.text:
                filter.click()
                print(f'Фильтр: {needed_filter} включен')
                return None
        print(f'Фильтр: {needed_filter} не найден')

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

    def print_info_about_hotel(self, count_hotel: int = 10) -> None:
        """
        Выводит информацию об отелях
        :param count_hotel: кол-во отелей о которых выведется информация
        """
        self._get_hotels()
        for hotel in self.hotels[:count_hotel]:
            print(hotel.find_element(*SearchResultPageLocators.HOTEL_NAME).text)
            print(hotel.find_element(*SearchResultPageLocators.HOTEL_PRICE).text)
            print(hotel.find_element(*SearchResultPageLocators.HOTEL_SCORE).text)
            print('----------------------')

    def select_cities(self) -> None:
        """
        Выбирает в фильтре о городах первые 20 штук
        """
        for position in range(20):
            cities = self.find_elements(SearchResultPageLocators.CITIES)
            try:
                cities[position].click()
            except IndexError:
                print('Столько городов нет')
                break
            sleep(8)
