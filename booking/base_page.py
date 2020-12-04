from typing import List

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from booking.locators import BasePageLocators


class BasePage:
    """
    Реализации паттерна PageObject.
    Класс представляет собой базовый набор функций для работы с каждой страницей

    :atribute: url - ссылка на главный сайт с которым ведется работа
    :atribute: driver - драйвер через который ведется работа с браузером
    """
    url = 'https://www.booking.com/index.ru.html'
    driver = None

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def find_element(self, locator, timeout: int = 5) -> WebElement:
        """
        Находит элемент с данным локатором
        :param locator: Локатор элемента вида: (By.XPATH, '//div')
        :param timeout: Время на поиск локатора
        :return: Обьект WebElement найденный по локатору
        """
        element = WebDriverWait(self.driver, timeout=timeout).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator, timeout: int = 5) -> List[WebElement]:
        """
        Находит элементы с данным локатором
        :param locator: Локатор элемента вида: (By.XPATH, '//div')
        :param timeout: Время на поиск локатора
        :return: Список Обьектов WebElement найденный по локатору
        """
        elements = WebDriverWait(self.driver, timeout=timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def go_to_main_page(self):
        """
        Открывает главную страницу Booking
        """
        self.driver.get(self.url)

    def close_browser(self):
        """
        Закрывает браузер
        """
        self.driver.close()

    def close_cookies(self):
        """
        Закрывает всплываюшее уведомление о cookies-ах
        """
        button = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(BasePageLocators.COOKIES_BUTTON_NO))
        button.click()
