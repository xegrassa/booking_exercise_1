from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIES_BUTTON_NO = (By.CSS_SELECTOR, '#onetrust-reject-all-handler')

    CURRENCY_BUTTON = (
        By.XPATH, '//*[@data-tooltip-text="Выберите валюту"] | //*[@data-title="Выберите валюту"]')
    SELECT_RUB_CURRENCY = (
        By.XPATH, '//a/div/div[contains(text(), "Российский рубль")] | //*[contains(text(), "Российский рубль")]')

    LANGUAGE_BUTTON = (By.XPATH, '//*[@data-title="Выберите язык"]')

    def SELECT_COUNTRY_LANGUAGE(country_abbreviation: str = 'ru'):
        return (By.XPATH, f'//li[@data-lang="{country_abbreviation}"]')

    DESTINATION_FIELD = (By.XPATH, '//input[@type="search"]')
    CALENDAR_BUTTON = (By.XPATH, '//div[@class="xp__dates-inner"]')
    MONTHS = (By.XPATH, '//div[@class="bui-calendar__wrapper"]')
    MONTH_NAME = (By.XPATH, '//div[@class="bui-calendar__month"]')

    def SELECT_CERTAIN_DATE(date: str):
        return (By.XPATH, f'//td[@data-date="{date}"]')

    NEXT_MONTH_BUTTON = (By.XPATH, '//div[@data-bui-ref="calendar-next"]')

    GUEST_MENU = (By.XPATH, '//div[@class="xp__input-group xp__guests"]')
    ADD_GUEST_BUTTON = (By.XPATH,
                        '//div[@class="sb-group__field sb-group__field-adults"]/div/div[2]/button[@data-bui-ref="input-stepper-add-button"]')
    DECREASE_GUEST_BUTTON = (By.XPATH,
                             '//div[@class="sb-group__field sb-group__field-adults"]/div/div[2]/button[@data-bui-ref="input-stepper-subtract-button"]')
    GUEST_COUNT = (
    By.XPATH, '//div[@class="sb-group__field sb-group__field-adults"]/div/div[2]/span[@class="bui-stepper__display"]')

    CHECK_PRICE_BUTTON = (By.XPATH, '//div[@class="xp__button"]')

class SearchResultPageLocators:
    FORM_SEARCH_FILTER = (By.XPATH, '//form[@id="filterbox_wrap"]')
    FILTERS = (By.XPATH, '//div[@class="filteroptions"]//span[contains(@class, "filter_label")]')
    CITIES = (By.XPATH, '//div[@id="filter_uf"]//span[contains(@class,"filter_label")]')
    HOTELS = (By.XPATH, '//div[@data-hotelid]')
    HOTEL_NAME = (By.XPATH, './/span[contains(@class, "sr-hotel__name")]')
    HOTEL_PRICE = (By.XPATH, './/div[contains(@class, "bui-price-display__value ")]')
    HOTEL_SCORE = (By.XPATH, './/div[@class="bui-review-score__badge"]')