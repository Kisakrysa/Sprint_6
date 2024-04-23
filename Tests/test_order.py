import allure
import pytest

from Pages.order_page import OrderPages
from Tests.data import order_data_top_button, order_data_bottom_button


class TestOrder:

    @allure.title('Проверка оформления заказа через кнопку в шапке сайта')
    @pytest.mark.parametrize('name, lastname, address, telephone, delivery', order_data_top_button)
    def test_order_positive_top_button(self, driver, name, lastname, address, telephone, delivery):
        page = OrderPages(driver)
        page.open()
        page.button_cookie()

        page.order_button_click()
        page.order(name, lastname, address, telephone, delivery)
        assert page.return_order_is_processed().is_displayed()

    @allure.title('Проверка оформления заказа через кнопку в нижней части страницы')
    @pytest.mark.parametrize('name, lastname, address, telephone, delivery', order_data_bottom_button)
    def test_order_scooter_from_bottom_button(self, driver, name, lastname, address, telephone, delivery):
        page = OrderPages(driver)
        page.open()
        page.button_cookie()

        page.order_button_click()
        page.order(name, lastname, address, telephone, delivery)
        assert page.return_order_is_processed().is_displayed()