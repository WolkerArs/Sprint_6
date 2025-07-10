import allure
import pytest

import curl
from conftest import to_order_page
from data import Credentials

from pages.order_page import OrderPage
from pages.main_page import MainPage

class TestGetOrderPage:

    @allure.title('Переход на страницу Дзена')
    def test_get_order_page_from_logo_button(self, to_order_page, driver):
        driver = to_order_page
        order_page = OrderPage(driver)
        order_page.click_logo_yandex()
        assert driver.current_url == curl.dzen_page

    @allure.title('Переход на главную страницу Самоката')
    def test_get_main_page_from_logo_button(self, to_order_page, driver):
        driver = to_order_page
        order_page = OrderPage(driver)
        order_page.click_logo_scooter()
        assert driver.current_url == curl.main_page + '/'

class TestMakeNewOrder:

    @allure.title('Создание нового заказа')
    @pytest.mark.parametrize('name, '
                             'surname, '
                             'location, '
                             'metro, '
                             'number, '
                             'date, '
                             'period, '
                             'color, '
                             'comment',
                             Credentials.credential)
    def test_make_new_order(self,
                            to_order_page,
                            driver,
                            name,
                            surname,
                            location,
                            metro,
                            number,
                            date,
                            period,
                            color,
                            comment):
        driver = to_order_page
        order_page = OrderPage(driver)
        order_page.fill_the_form_order_page_one(name,surname,location,metro,number)
        order_page.fill_the_form_order_page_two(date,period,color,comment)
        popup_text = order_page.get_order_popup_text()
        assert 'Заказ оформлен' in popup_text





