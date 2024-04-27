import allure

from Pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPages(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Нажимаем кнопку "Заказать" в шапке')
    def order_button_click(self):
        self.find_element(*OrderPageLocators.button_order).click()

    @allure.step('Нажимаем кнопку "Заказать" внизу страницы')
    def order_bottom_button_click(self):
        self.find_element(*OrderPageLocators.button_order).click()

    @allure.step('Вводим имя')
    def name_order_send(self, name_text):
        self.find_element(*OrderPageLocators.name_order).send_keys(name_text)

    @allure.step('Вводим фамилию')
    def lastname_order_send(self, lastname):
        self.find_element(*OrderPageLocators.lastname_order).send_keys(lastname)

    @allure.step('Вводим адрес')
    def address_order_send(self, address):
        self.find_element(*OrderPageLocators.address_order).send_keys(address)

    @allure.step('Нажимаем на поле "Станция метро')
    def metro_station_click(self):
        self.find_element(*OrderPageLocators.metro_station_order).click()

    @allure.step('Выбираем станцию "Бульвар Рокоссовского')
    def station_click(self):
        self.find_element(*OrderPageLocators.station).click()

    @allure.step('Вводим номер телефона')
    def telephone_order_send(self, telephone):
        self.find_element(*OrderPageLocators.telephone_order).send_keys(telephone)

    @allure.step('Yажимаем кнопку "Далее"')
    def next_button_order_click(self):
        self.find_element(*OrderPageLocators.next_button_order).click()

    @allure.step('Указываем дату когда привезти самокат')
    def delivery_order_send(self,delivery):
        self.find_element(*OrderPageLocators.delivery_order).send_keys(delivery)

    @allure.step('Закрываем календарь')
    def close_calendar_order_click(self):
        self.find_element(*OrderPageLocators.close_calendar_order).click()

    @allure.step('Нажимаем на поле "Срок аренды"')
    def period_order_click(self):
        self.find_element(*OrderPageLocators.period_order).click()

    @allure.step('Выбираем срок аренды "Сутки"')
    def day_order_click(self):
        self.find_element(*OrderPageLocators.day_order).click()

    @allure.step('Выбираем цвет самоката')
    def color_order_click(self):
        self.find_element(*OrderPageLocators.color_order).click()

    @allure.step('Нажимаем кнопку "Заказать" под формой')
    def button_click(self):
        self.find_element(*OrderPageLocators.button).click()

    @allure.step('Нажимаем кнопку "Да" в окне оформления заказ')
    def button_yes_order_click(self):
        self.find_element(*OrderPageLocators.button_yes_order).click()

    # Метод возвращает "Заказ успешно оформлен"
    def return_order_is_processed(self):
        return self.find_element(*OrderPageLocators.order_is_processed)

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