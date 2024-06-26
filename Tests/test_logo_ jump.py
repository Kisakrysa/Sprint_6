import time

import allure

from Pages.questions_page import QuestionPage
from Tests.settings import URL, URL_DZEN


class TestLogoJump:

    @allure.title('Проверка перехода на домашнюю страницу')
    def test_logo_redirects_to_home(self, driver):
        jump_from_page = QuestionPage(driver)
        jump_from_page.open()
        jump_from_page.button_cookie()

        jump_from_page.logo_click()
        assert jump_from_page.get_current_url() == URL

    @allure.title('Проверка перехода на страницу Дзена по логотипу Я')
    def test_yandex_logo_redirects_to_zen(self, driver):
        jump_from_page = QuestionPage(driver)
        jump_from_page.open()
        jump_from_page.button_cookie()

        jump_from_page.logo_yandex_click()
        time.sleep(3)
        jump_from_page.switch_to_new_tab()
        time.sleep(3)
        assert jump_from_page.get_current_url() == URL_DZEN
