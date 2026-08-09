import pytest
import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from helpers import login_registered_user
from data import TestData
from locators.order_feed_locators import OrderFeedLocators
import time


@allure.epic("UI Тесты")
@allure.feature("Лента заказов")
class TestOrderFeed:
    
    @allure.title('При создании заказа счётчик «Выполнено за всё время» увеличивается')
    def test_total_orders_counter_increases(self, pages, login):
        pages.click_orders_list_button()
        order_feed_page = OrderFeedPage(pages.driver)
        prev_counter_value = order_feed_page.get_total_order_count_daily(OrderFeedLocators.TOTAL_ORDER_COUNT)
        pages.click_constructor_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_modal_order()
        time.sleep(1)
        pages.click_orders_list_button()
        time.sleep(2)
        current_counter_value = order_feed_page.get_total_order_count_daily(OrderFeedLocators.TOTAL_ORDER_COUNT)
        assert current_counter_value > prev_counter_value

    @allure.title('При создании заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_today_orders_counter_increases(self, pages, login):
        pages.click_orders_list_button()
        order_feed_page = OrderFeedPage(pages.driver)
        prev_counter_value = order_feed_page.get_total_order_count_daily(OrderFeedLocators.DAILY_ORDER_COUNT)
        pages.click_constructor_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_modal_order()
        time.sleep(1)
        pages.click_orders_list_button()
        time.sleep(2)
        current_counter_value = order_feed_page.get_total_order_count_daily(OrderFeedLocators.DAILY_ORDER_COUNT)
        assert current_counter_value > prev_counter_value

    @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
    def test_new_order_appears_in_work_list(self, pages, login):
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_modal_order()
        time.sleep(1)
        pages.click_orders_list_button()
        time.sleep(2)
        order_in_progress = pages.get_user_order_in_progress()
        assert order_in_progress != ""