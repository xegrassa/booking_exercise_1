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
    MONTHS = (By.XPATH, '//div[@class="bui-calendar__wrapper"]')
    MONTH_NAME = (By.XPATH, '//div[@class="bui-calendar__month"]')

    def SELECT_CERTAIN_DATE(date: str):
        return (By.XPATH, f'//td[@data-date="{date}"]')

    NEXT_MONTH_BUTTON = (By.XPATH, '//div[@data-bui-ref="calendar-next"]')
