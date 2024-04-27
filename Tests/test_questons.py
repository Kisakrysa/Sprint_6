import time

import allure
import pytest
from conftest import driver
from Pages.questions_page import MainPageQuests, MainPageAnswers


class TestQuestions:

    @allure.title("Проверка Вопроса {quest_number}")
    @allure.description("Проверяем что каждый вопрос раскрывается при нажатии на него")
    @pytest.mark.parametrize("quest_number, quest_element, answer_element, answer_text", [
        (0, MainPageQuests.QUEST_1, MainPageAnswers.answer_text_1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (1, MainPageQuests.QUEST_2, MainPageAnswers.answer_text_2, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (2, MainPageQuests.QUEST_3, MainPageAnswers.answer_text_3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (3, MainPageQuests.QUEST_4, MainPageAnswers.answer_text_4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (4, MainPageQuests.QUEST_5, MainPageAnswers.answer_text_5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (5, MainPageQuests.QUEST_6, MainPageAnswers.answer_text_6, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (6, MainPageQuests.QUEST_7, MainPageAnswers.answer_text_7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (7, MainPageQuests.QUEST_8, MainPageAnswers.answer_text_8, "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
    ])


    def test_click_quest(self, driver, quest_number, quest_element, answer_element, answer_text):
        main_page_quest = MainPageQuests(driver)
        main_page_answer = MainPageAnswers(driver)
        main_page_quest.open()
        main_page_quest.button_cookie()
        time.sleep(3)
        main_page_quest.scroll_to_quest(quest_element)
        main_page_quest.find_and_click_quest(quest_element)

        assert main_page_answer.find_answer(answer_element)
