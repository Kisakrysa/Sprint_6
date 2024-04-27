import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from Tests.settings import URL


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def wait_and_find_element(self, locator):
        WebDriverWait(self.browser, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.browser.find_element(*locator)

    def scroll_into_view(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def find_element(self, *args):
        return self.browser.find_element(*args)

    def wait(self, locator):
        WebDriverWait(self.browser, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.browser.find_element(*locator)

    @allure.step('Открываем страницу')
    def open(self):
        self.browser.get(URL)

    @allure.step('Нажимаем принять куки')
    # Принимаем куки
    def button_cookie(self):
        self.find_element(*OrderPageLocators.cookie).click()

    @allure.step('Получаем URL открытой страницы')
    def get_current_url(self):
        return self.browser.current_url

    @allure.step('Получаем список вопросов')
    def get_questions(self):
        return self.browser.find_elements(*MainPageLocators.question)

    @allure.step('Переключаемся на вкладку')
    def switch_to(self, window_index):
        all_windows = self.browser.window_handles
        self.browser.switch_to.window(all_windows[window_index])

    @allure.step('Переключаемся на вкладку V.2')
    def switch_to_new_tab(self):
        all_tabs = self.browser.window_handles
        new_tab = all_tabs[-1]
        self.browser.switch_to.window(new_tab)