import pytest
import allure
from data import TestData


@allure.epic("UI Тесты")
@allure.feature("Главная страница")
class TestMainPage:

    @allure.title('При нажатии в header кнопки «Лента заказов» совершается переход на страницу заказов')
    def test_redirection_to_order_list(self, pages):
        pages.click_orders_list_button()
        current_url = pages.get_current_url()
        assert current_url == TestData.ORDER_FEED_URL

    @allure.title('При нажатии в header кнопки "Конструктор" совершается переход на страницу сбора бургера')
    def test_go_to_constructor(self, pages):
        pages.click_orders_list_button()
        pages.click_constructor_button()
        current_url = pages.get_current_url()
        assert current_url == TestData.BASE_URL

    @allure.title('При нажатии на ингредиент всплывает окно с информацией')
    def test_popup_of_ingredient(self, pages):
        pages.click_on_ingredient()
        actually_text = pages.check_show_window_with_details()
        assert actually_text == "Детали ингредиента"

    @allure.title('При нажатии в модальном окне с информацией об ингредиенте крестика, окно закрывается')
    def test_close_ingredient_details_window(self, pages):
        pages.click_on_ingredient()
        pages.click_cross_button()
        pages.invisibility_ingredient_details()
        assert pages.check_displayed_ingredient_details() == False

    @allure.title('При добавлении ингредиента в заказ, счетчик увеличивается')
    def test_ingredient_counter(self, pages):
        prev_counter_value = pages.get_count_value()
        pages.add_filling_to_order()
        actual_value = pages.get_count_value()
        assert actual_value > prev_counter_value