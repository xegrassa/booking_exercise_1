from time import sleep
from typing import List

from selenium.webdriver.remote.webelement import WebElement

from booking.base_page import BasePage
from booking.locators import SearchResultPageLocators


class SearchResultPage(BasePage):
    filters: List[WebElement] = None
    hotels: List[WebElement] = None

    def select_filter(self, needed_filter: str):
        self._get_filters()
        for filter in self.filters:
            if needed_filter in filter.text:
                filter.click()
                print(f'Фильтр: {needed_filter} включен')
                return None
        print(f'Фильтр: {needed_filter} не найден')

    def _get_filters(self):
        self.filters = self.find_elements(SearchResultPageLocators.FILTERS)

    def _get_hotels(self):
        self.hotels = self.find_elements(SearchResultPageLocators.HOTELS)

    def print_info_about_hotel(self, count_hotel: int = 10):
        self._get_hotels()
        for hotel in self.hotels[:count_hotel]:
            print(hotel.find_element(*SearchResultPageLocators.HOTEL_NAME).text)
            print(hotel.find_element(*SearchResultPageLocators.HOTEL_PRICE).text)
            print(hotel.find_element(*SearchResultPageLocators.HOTEL_SCORE).text)
            print('----------------------')

    def select_cities(self):
        for position in range(5):
            cities = self.find_elements(SearchResultPageLocators.CITIES)
            try:
                cities[position].click()
            except IndexError:
                print('Столько городов нет')
                break
            sleep(8)
