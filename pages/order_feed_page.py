from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    
    def click_order(self):
        self.click_on_element(OrderFeedLocators.ORDER_LINK)
    
    def check_order_structure(self):
        try:
            self.wait_until_element_visibility(OrderFeedLocators.ORDER_STRUCTURE)
            return True
        except:
            return False
    
    def get_total_order_count_daily(self, counter):
        try:
            self.wait_until_element_visibility(counter)
            text = self.get_actually_text(counter)
            return int(text) if text else 0
        except:
            return 0