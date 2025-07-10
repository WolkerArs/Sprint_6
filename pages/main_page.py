import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class MainPage(BasePage):

    #кнопки Заказать
    top_order_button = [By.CLASS_NAME, 'Button_Button__ra12g']
    bottom_order_button = [By.XPATH,
                           './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
                           '[text()="Заказать"]']

    #элементы выпадающего списка Вопросы о важном

    @staticmethod
    def faq_element(element_number):
        return By.XPATH, f'.//div[@id="accordion__heading-{element_number}"]'

    @staticmethod
    def faq_element_text(element_number):
        return By.XPATH, f'.//div[@id="accordion__panel-{element_number}"]//p'

    @allure.step('Нажать на верхнюю кнопку "Заказать"')
    def click_on_top_order_button(self):
        self.click_on_element(self.top_order_button)

    @allure.step('Нажать на нижнюю кнопку "Заказать"')
    def click_on_bottom_order_button(self):
        self.scroll_to_element(self.bottom_order_button)
        self.click_on_element(self.bottom_order_button)

    @allure.step('Нажать на элемент "Вопросы о важном"')
    def click_on_faq_element(self, element_number):
        self.scroll_to_element(self.faq_element(element_number))
        self.click_on_element(self.faq_element(element_number))

    @allure.step('Найти текст ответа из FAQ')
    def get_text_of_faq_answer(self, element_number):
        return self.get_text_on_element(self.faq_element_text(element_number))





