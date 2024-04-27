from selenium.webdriver.common.by import By


class MainPageLocators:
    cookie = (By.ID, 'rcc-confirm-button')
    question = (By.CLASS_NAME, 'accordion__item')
    answer = (By.CSS_SELECTOR, '.accordion__panel p')
    logo = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    logo_dzen = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')