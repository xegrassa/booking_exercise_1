import datetime

from selenium.common.exceptions import TimeoutException

from booking.header import Header
from booking.locators import MainPageLocators
from booking.search_result_page import SearchResultPage


class MainPage(Header):
    """
    Реализации паттерна PageObject.
    Класс представляет собой главную страницу
    """

    def open_calendar(self) -> None:
        """
        Открыть таблицу дат путешествия
        """
        self.find_element(MainPageLocators.CALENDAR_BUTTON).click()

    def open_guest_menu(self) -> None:
        """
        Открыть таблицу количества посетителей
        """
        self.find_element(MainPageLocators.GUEST_MENU).click()

    def input_destination(self, destination: str) -> None:
        """
        Вводит в поле место поездки город/страну назначения
        :param destination: город/страна назначения
        """
        self.find_element(MainPageLocators.DESTINATION_FIELD).send_keys(destination)

    def click_check_price(self) -> SearchResultPage:
        """
        Нажимает кнопку проверить цену
        :return: страницу с найденными выриантами
        """
        self.find_element(MainPageLocators.CHECK_PRICE_BUTTON).click()
        return SearchResultPage(self.driver)

    def select_date(self, date: str) -> None:
        """
        Выбирает дату путешествия
        :param date: дата которую надо выбрать
        """
        certain_date = datetime.date.fromisoformat(date)
        locator = MainPageLocators.SELECT_CERTAIN_DATE(str(certain_date))
        while True:
            try:
                self.find_element(locator).click()
                break
            except TimeoutException:
                self._click_next_month()

    def _click_next_month(self) -> None:
        """
        При открытой таблице календаря нажимает кнопку следующего месяца
        """
        self.find_element(MainPageLocators.NEXT_MONTH_BUTTON).click()

    def select_guest(self, need_guest: int) -> None:
        """
        Выбирает нужное количество гостей
        :param need_guest: количество гостей которое нужно
        """
        while True:
            if need_guest == self._get_guest_count():
                break
            if need_guest > self._get_guest_count():
                self._add_guest()
            else:
                self._decrease_guest()

    def _decrease_guest(self) -> None:
        """
        При открытой таблице гостей нажимает кнопку уменьшения
        """
        self.find_element(MainPageLocators.DECREASE_GUEST_BUTTON).click()

    def _add_guest(self) -> None:
        """
        При открытой таблице гостей нажимает кнопку увеличения
        """
        self.find_element(MainPageLocators.ADD_GUEST_BUTTON).click()

    def _get_guest_count(self) -> int:
        """
        Возвращает количество гостей выбранного на данный момент
        :return: количество гостей
        """
        return int(self.find_element(MainPageLocators.GUEST_COUNT).text)
