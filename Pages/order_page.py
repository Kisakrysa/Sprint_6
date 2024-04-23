import allure

from Pages.home_page import MainPage
from Tests.locators import OrderPage


class OrderPages(MainPage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Нажимаем кнопку "Заказать" в шапке')
    def order_button_click(self):
        self.find_element(*OrderPage.button_order).click()

    @allure.step('Нажимаем кнопку "Заказать" внизу страницы')
    def order_bottom_button_click(self):
        self.find_element(*OrderPage.button_order).click()

    @allure.step('Вводим имя')
    def name_order_send(self, name_text):
        self.find_element(*OrderPage.name_order).send_keys(name_text)

    @allure.step('Вводим фамилию')
    def lastname_order_send(self, lastname):
        self.find_element(*OrderPage.lastname_order).send_keys(lastname)

    @allure.step('Вводим адрес')
    def address_order_send(self, address):
        self.find_element(*OrderPage.address_order).send_keys(address)

    @allure.step('Нажимаем на поле "Станция метро')
    def metro_station_click(self):
        self.find_element(*OrderPage.metro_station_order).click()

    @allure.step('Выбираем станцию "Бульвар Рокоссовского')
    def station_click(self):
        self.find_element(*OrderPage.station).click()

    @allure.step('Вводим номер телефона')
    def telephone_order_send(self, telephone):
        self.find_element(*OrderPage.telephone_order).send_keys(telephone)

    @allure.step('Yажимаем кнопку "Далее"')
    def next_button_order_click(self):
        self.find_element(*OrderPage.next_button_order).click()

    @allure.step('Указываем дату когда привезти самокат')
    def delivery_order_send(self,delivery):
        self.find_element(*OrderPage.delivery_order).send_keys(delivery)

    @allure.step('Закрываем календарь')
    def close_calendar_order_click(self):
        self.find_element(*OrderPage.close_calendar_order).click()

    @allure.step('Нажимаем на поле "Срок аренды"')
    def period_order_click(self):
        self.find_element(*OrderPage.period_order).click()

    @allure.step('Выбираем срок аренды "Сутки"')
    def day_order_click(self):
        self.find_element(*OrderPage.day_order).click()

    @allure.step('Выбираем цвет самоката')
    def color_order_click(self):
        self.find_element(*OrderPage.color_order).click()

    @allure.step('Нажимаем кнопку "Заказать" под формой')
    def button_click(self):
        self.find_element(*OrderPage.button).click()

    @allure.step('Нажимаем кнопку "Да" в окне оформления заказ')
    def button_yes_order_click(self):
        self.find_element(*OrderPage.button_yes_order).click()

    # Метод возвращает "Заказ успешно оформлен"
    def return_order_is_processed(self):
        return self.find_element(*OrderPage.order_is_processed)

    # Метод объединяет остальные в шаг
    def order(self, customer_name, lastname, address, telephone, delivery):
        self.name_order_send(customer_name)
        self.lastname_order_send(lastname)
        self.address_order_send(address)
        self.metro_station_click()
        self.station_click()
        self.telephone_order_send(telephone)
        self.next_button_order_click()
        self.delivery_order_send(delivery)
        self.close_calendar_order_click()
        self.period_order_click()
        self.day_order_click()
        self.color_order_click()
        self.button_click()
        self.button_yes_order_click()