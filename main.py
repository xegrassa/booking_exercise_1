import configparser
import os.path
from time import sleep
from selenium import webdriver
from booking.locators import MainPageLocators
from booking.main_page import MainPage

CHROME_DRIVER = os.path.join(os.getcwd(), 'webdrivers', 'chromedriver')
CONFIG_PATH = 'booking.ini'


def parse_booking_config() -> dict:
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    return {'user_count': config.getint('booking.com', 'user_count'),
            'data_in': config.get('booking.com', 'data_in'),
            'data_out': config.get('booking.com', 'data_out'),
            'country': config.get('booking.com', 'country')}


def main():
    args = parse_booking_config()

    driver = webdriver.Chrome(CHROME_DRIVER)
    page = MainPage(driver=driver)
    page.go_to_main_page()
    sleep(3)
    page.close_cookies()
    # page.open_currency()
    # page.click_to_RUB()
    # sleep(1)
    # page.open_language()
    # page.click_to_language(args['country'])
    # sleep(3)

    page.open_calendar()
    month = page.get_months()
    print(month)
    sleep(5)





    page.close_browser()
    print('ALL OKEY')


if __name__ == '__main__':
    main()
