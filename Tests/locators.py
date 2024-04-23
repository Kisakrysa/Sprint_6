from selenium.webdriver.common.by import By

class HomePage:
    cookie = (By.ID, 'rcc-confirm-button')
    question = (By.CLASS_NAME, 'accordion__item')
    answer = (By.CSS_SELECTOR, '.accordion__panel p')
    logo = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    logo_dzen = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
class OrderPage:
    # Локаторы элементов на странице заполнени формы заказа
    cookie = (By.ID, 'rcc-confirm-button')
    button_order = (By.CLASS_NAME, 'Button_Button__ra12g')
    name_order = (By.CSS_SELECTOR, '[placeholder="* Имя"]')
    lastname_order = (By.CSS_SELECTOR, '[placeholder="* Фамилия"]')
    address_order = (By.CSS_SELECTOR, '[placeholder="* Адрес: куда привезти заказ"]')
    metro_station_order = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')
    station = (By.CSS_SELECTOR, 'div.Order_Text__2broi')
    telephone_order = (By.CSS_SELECTOR, '[placeholder="* Телефон: на него позвонит курьер"]')
    next_button_order = (By.XPATH, "//button[text()='Далее']")
    delivery_order = (By.CSS_SELECTOR, '[placeholder="* Когда привезти самокат"]')
    period_order = (By.CSS_SELECTOR, '.Dropdown-placeholder')
    day_order = (By.XPATH, "//div[@class='Dropdown-option'and text()='сутки']")
    color_order = (By.ID, 'black')
    button = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    close_calendar_order = (By.XPATH, "//div[@class='App_App__15LM-']")
    button_yes_order = (By.XPATH, "//button[text()='Да']")
    order_is_processed = (By.XPATH, "//div[@class='Order_Text__2broi']")
    bottom_button = (By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")
