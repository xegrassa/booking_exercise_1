from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from booking.locators import MainPageLocators


class BasePage:
    url = 'https://www.booking.com/index.ru.html'
    driver = None

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def find_element(self, locator) -> WebElement:
        element = WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator):
        elements = WebDriverWait(self.driver, timeout=5).until(EC.presence_of_all_elements_located(locator))
        return elements

    def go_to_main_page(self):
        self.driver.get(self.url)

    def close_browser(self):
        self.driver.close()

    def close_cookies(self):
        button = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(MainPageLocators.COOKIES_BUTTON_NO))
        button.click()
