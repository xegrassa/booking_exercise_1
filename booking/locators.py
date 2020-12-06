from selenium.webdriver.common.by import By


class BasePageLocators:
    COOKIES_BUTTON_NO = (By.CSS_SELECTOR, '#onetrust-reject-all-handler')


class HeaderLocators:
    CURRENCY_BUTTON = (
        By.XPATH, '//*[@data-tooltip-text="Выберите валюту"] | //*[@data-title="Выберите валюту"]')
    SELECT_RUB_CURRENCY = (By.XPATH,
                           '//li[contains(@class, "currency_RUB")] | //*[contains(@class,"bui-traveller-header__currency")][contains(text(),"RUB")]')
    LANGUAGE_BUTTON = (By.XPATH, '//*[@data-title="Выберите язык"] | //*[@data-modal-id="language-selection"]')

    def SELECT_COUNTRY_LANGUAGE(country_abbreviation: str = 'ru'):
        return (By.XPATH,
                f'//li[@data-lang="{country_abbreviation}"] | //div[@class="bui-modal__inner"]//div[@lang="{country_abbreviation}"]')


class MainPageLocators:
    DESTINATION_FIELD = (By.XPATH, '//input[@type="search"]')
    CALENDAR_BUTTON = (By.XPATH, '//div[@class="xp__dates-inner"]')

    def SELECT_CERTAIN_DATE(date: str):
        return (By.XPATH, f'//td[@data-date="{date}"]')

    NEXT_MONTH_BUTTON = (By.XPATH, '//div[@data-bui-ref="calendar-next"]')

    GUEST_MENU = (By.XPATH, '//div[@class="xp__input-group xp__guests"]')
    ADD_GUEST_BUTTON = (By.XPATH,
                        '//div[@class="sb-group__field sb-group__field-adults"]/div/div[2]/button[@data-bui-ref="input-stepper-add-button"]')
    DECREASE_GUEST_BUTTON = (By.XPATH,
                             '//div[@class="sb-group__field sb-group__field-adults"]/div/div[2]/button[@data-bui-ref="input-stepper-subtract-button"]')
    GUEST_COUNT = (
        By.XPATH,
        '//div[@class="sb-group__field sb-group__field-adults"]/div/div[2]/span[@class="bui-stepper__display"]')

    CHECK_PRICE_BUTTON = (By.XPATH, '//div[@class="xp__button"]')


class SearchResultPageLocators:
    FILTERS = (By.XPATH, '//div[@class="filteroptions"]//span[contains(@class, "filter_label")]')

    CITIES = (By.XPATH, '//div[@id="filter_uf"]/div[@class="filteroptions"]')
    CITY = (By.XPATH, './/a')
    MORE_BUTTON = (By.XPATH, '//div[@id="filter_uf"]//button[contains(@class, "more")]')
    SPINER = (By.XPATH, '//div[contains(@class,"sr-usp-overlay__container")]')

    HOTELS = (By.XPATH, '//div[@data-hotelid]')
    HOTEL_NAME = (By.XPATH, './/span[contains(@class, "sr-hotel__name")]')
    HOTEL_PRICE = (By.XPATH, './/div[contains(@class, "bui-price-display__value ")]')
    HOTEL_SCORE = (By.XPATH, './/div[@class="bui-review-score__badge"]')
