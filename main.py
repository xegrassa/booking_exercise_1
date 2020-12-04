import configparser
import os.path
from time import sleep

from selenium import webdriver

from booking.main_page import MainPage

CHROME_DRIVER = os.path.join(os.getcwd(), 'webdrivers', 'chromedriver')
CONFIG_PATH = 'booking.ini'


def parse_booking_config() -> dict:
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH, encoding='utf8')
    return {'guest_count': config.getint('booking.com', 'guest_count'),
            'date_in': config.get('booking.com', 'date_in'),
            'date_out': config.get('booking.com', 'date_out'),
            'country': config.get('booking.com', 'country'),
            'destination': config.get('booking.com', 'destination'),
            'filters': config.get('booking_filter', 'filters').replace('\n', '|').split("|")}


def main():
    args = parse_booking_config()

    driver = webdriver.Chrome(CHROME_DRIVER)
    page = MainPage(driver=driver)
    page.go_to_main_page()
    sleep(3)
    page.close_cookies()

    page.click_to_RUB()
    page.click_to_language(args['country'])
    page.input_destination(args['destination'])
    page.open_calendar()
    page.select_date(args['date_in'])
    page.select_date(args['date_out'])
    page.open_guest_menu()
    page.select_guest(args['guest_count'])

    search_page = page.click_check_price()
    search_page.select_cities()
    search_page.select_filter(args['filters'])
    search_page.print_info_about_hotel()

    sleep(10)
    search_page.close_browser()
    print('ALL OKEY')


if __name__ == '__main__':
    main()
