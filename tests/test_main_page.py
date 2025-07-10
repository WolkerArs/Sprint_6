import allure
import pytest

import curl
from data import QuestionNumbers

from pages.main_page import MainPage

class TestMainPageFAQ:

    @allure.title('Открытие вкладки FAQ')
    @pytest.mark.parametrize('element, answer_text', QuestionNumbers.element)
    def test_faq_questions(self, driver, element, answer_text):
        main_page = MainPage(driver)
        main_page.click_on_faq_element(element)
        current_text = main_page.get_text_of_faq_answer(element)
        assert current_text == answer_text

    @allure.title('Открытие страницы заказа с верхней кнопки "Заказать"')
    def test_open_order_page_from_top_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_top_order_button()
        assert driver.current_url == curl.order_page

    @allure.title('Открытие страницы заказа с нижней кнопки "Заказать"')
    def test_open_order_page_from_bottom_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bottom_order_button()
        assert driver.current_url == curl.order_page
