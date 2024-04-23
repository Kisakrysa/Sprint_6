import allure
import pytest

from Tests.locators import HomePage
from Pages.questions_page import QuestionPage
from Tests.data import answer_text_1, answer_text_2, answer_text_3, answer_text_4, answer_text_5, answer_text_6, \
    answer_text_7, answer_text_8


class TestQuestions:

    @pytest.mark.parametrize("question_index, answer_index, expected_answer", [
        (0, 0, answer_text_1),
        (1, 1, answer_text_2),
        (2, 2, answer_text_3),
        (3, 3, answer_text_4),
        (4, 4, answer_text_5),
        (5, 5, answer_text_6),
        (6, 6, answer_text_7),
        (7, 7, answer_text_8)
    ])
    @allure.title('Проверка ответа на вопрос')
    def test_question_open_answer(self, driver, question_index, answer_index, expected_answer):
        questions_page = QuestionPage(driver)
        questions_page.open()
        questions_page.button_cookie()

        questions_page.click_question_by_index(question_index)
        questions_page.wait(HomePage.question)
        actual_answer = questions_page.get_text_of_answer_by_index(answer_index)
        assert actual_answer == expected_answer
