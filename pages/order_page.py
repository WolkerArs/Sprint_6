import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class OrderPage(BasePage):

    # заголовок страницы
    header_text = [By.LINK_TEXT, 'Для кого самокат']

    yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    scooter_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    dzen_page_logo = [By.CLASS_NAME, 'dzen-layout--desktop-base-header__logoLink-2h']

    # поля формы
    name_field = [By.XPATH, './/input[@placeholder="* Имя"]']
    surname_field = [By.XPATH, './/input[@placeholder="* Фамилия"]']
    location_field = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']
    number_field = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']

    metro_field = [By.XPATH, './/input[@placeholder="* Станция метро"]']
    metro_input_element = [By.XPATH, ".//li[@class='select-search__row']"]

    date_field = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']
    day_on_calendar = [By.XPATH, './/div[@tabindex="0"][@role="button"]']
    rental_period_field = [By.CLASS_NAME, 'Dropdown-placeholder']

    @staticmethod
    def rental_period_element (period):
        return [By.XPATH, f'.//div[@class="Dropdown-option"][text()="{period}"]']

    @staticmethod
    def choose_color(color):
        return [By.ID, f'{color}']

    comment_field = [By.XPATH, './/input[@placeholder="Комментарий для курьера"]']

    # кнопка Далее
    next_page_order_button = [By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
                                      '[text()="Далее"]']

    # кнопка подтверждения заказа
    confirm_order_button = [By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
                                      '[text()="Заказать"]']
    yes_order_button = [By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
                                  '[text()="Да"]']
    popup_order_header = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']

    @allure.step('Заполнить форму на первой странице заказа')
    def fill_the_form_order_page_one(self,
                                name,
                                surname,
                                location,
                                metro,
                                number):

        self.send_keys_to_input(self.name_field, name)
        self.send_keys_to_input(self.surname_field, surname)
        self.send_keys_to_input(self.location_field, location)
        self.send_keys_to_input(self.metro_field, metro)
        self.click_on_element(self.metro_input_element)
        self.send_keys_to_input(self.number_field, number)
        self.click_on_element(self.next_page_order_button)

    @allure.step('Заполнить форму на второй странице и подтвердить заказ')
    def fill_the_form_order_page_two(self,
                                date,
                                period,
                                color,
                                comment):

        self.send_keys_to_input(self.date_field, date)
        self.click_on_element(self.day_on_calendar)
        self.click_on_element(self.rental_period_field)
        self.click_on_element(self.rental_period_element(period))
        self.click_on_element(self.choose_color(color))
        self.send_keys_to_input(self.comment_field, comment)
        self.click_on_element(self.confirm_order_button)
        self.click_on_element(self.yes_order_button)

    @allure.step('Получить заголовок всплывающего окна об успешном заказе')
    def get_order_popup_text(self):
        return self.get_text_on_element(self.popup_order_header)

    @allure.step('Нажать на лого Яндекса и перейти на страницу Дзена')
    def click_logo_yandex(self):
        self.click_on_element(self.yandex_logo)
        self.switch_to_another_window(self.dzen_page_logo)

    @allure.step('Нажать на заголовок Самокат')
    def click_logo_scooter(self):
        self.click_on_element(self.scooter_logo)



