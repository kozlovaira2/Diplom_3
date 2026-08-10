from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
import allure


class OrderFeedPage(BasePage):
    
    @allure.step('Клик по заказу в ленте')
    def click_order(self):
        self.click_on_element(OrderFeedLocators.ORDER_LINK)
    
    @allure.step('Проверка структуры заказа')
    def check_order_structure(self):
        try:
            self.wait_until_element_visibility(OrderFeedLocators.ORDER_STRUCTURE)
            return True
        except:
            return False
    
    @allure.step('Получение значения счетчика заказов')
    def get_total_order_count_daily(self, counter):
        try:
            self.wait_until_element_visibility(counter)
            text = self.get_actually_text(counter)
            return int(text) if text else 0
        except:
            return 0