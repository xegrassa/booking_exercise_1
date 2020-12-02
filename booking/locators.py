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

    CALENDAR_BUTTON = (By.XPATH, '//div[@class="xp__dates-inner"]')
    MONTHS_CALENDAR = (By.XPATH, '//div[@class="bui-calendar__month"]')