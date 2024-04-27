import allure

from locators.main_page_locators import MainPageLocators
from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPageAnswers(BasePage):
    answer_text_1 = (By.XPATH, "//p[text() = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")
    answer_text_2 = (By.XPATH, "//p[text() = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']")
    answer_text_3 = (By.XPATH, "//p[text() = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']")
    answer_text_4 = (By.XPATH, "//p[text() = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")
    answer_text_5 = (By.XPATH, "//p[text() = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']")
    answer_text_6 = (By.XPATH, "//p[text() = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']")
    answer_text_7 = (By.XPATH, "//p[text() = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']")
    answer_text_8 = (By.XPATH, "//p[text() = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']")

    @allure.step('Ищем Ответ на Вопрос')
    def find_answer(self, answer_element):
        answer = self.wait_and_find_element(answer_element)
        return answer.is_displayed()


class MainPageQuests(BasePage):
    QUEST_1 = (By.XPATH, "//div[@id = 'accordion__heading-0']")
    QUEST_2 = (By.XPATH, "//div[@id = 'accordion__heading-1']")
    QUEST_3 = (By.XPATH, "//div[@id = 'accordion__heading-2']")
    QUEST_4 = (By.XPATH, "//div[@id = 'accordion__heading-3']")
    QUEST_5 = (By.XPATH, "//div[@id = 'accordion__heading-4']")
    QUEST_6 = (By.XPATH, "//div[@id = 'accordion__heading-5']")
    QUEST_7 = (By.XPATH, "//div[@id = 'accordion__heading-6']")
    QUEST_8 = (By.XPATH, "//div[@id = 'accordion__heading-7']")

    @allure.step('скролл до Вопроса')
    def scroll_to_quest(self, quest_element):
        quest = self.wait_and_find_element(quest_element)
        self.scroll_into_view(quest)

    @allure.step('Ищем Вопрос и кликаем на него')
    def find_and_click_quest(self, quest_element):
        quest = self.wait_and_find_element(quest_element)
        quest.click()


class QuestionPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Нажимаем на логотип "Самокат"')
    def logo_click(self):
        self.find_element(*MainPageLocators.logo).click()

    @allure.step('Нажимаем на на логотип "Яндекс"')
    def logo_yandex_click(self):
        self.find_element(*MainPageLocators.logo_dzen).click()





