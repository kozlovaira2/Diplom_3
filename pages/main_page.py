from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import TestData
import time


class MainPage(BasePage):
    
    # НАВИГАЦИЯ
    def click_orders_list_button(self):
        self.click_on_element(MainPageLocators.ORDERS_LIST_BUTTON)
        self.wait_until_element_visibility(OrderFeedLocators.ORDERS_LIST_TITLE)
    
    def click_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_until_element_visibility(MainPageLocators.MAIN_LIST_TITLE)
    
    def click_on_account(self):
        self.click_on_element(MainPageLocators.PROFILE_BUTTON)
    
    def click_login_button(self):
        self.click_on_element(MainPageLocators.LOGIN_BUTTON_MAIN)
    
    # ИНГРЕДИЕНТЫ
    def click_on_ingredient(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.BUN_INGREDIENT)
        self.click_on_element(MainPageLocators.BUN_INGREDIENT)
    
    def click_cross_button(self):
        self.move_to_element_and_click(MainPageLocators.CROSS_BUTTON)
    
    def get_count_value(self):
        try:
            self.wait_until_element_visibility(MainPageLocators.INGREDIENT_COUNTER)
            counter = self.driver.find_element(*MainPageLocators.INGREDIENT_COUNTER)
            return int(counter.text) if counter.text else 0
        except:
            return 0
    
    def add_filling_to_order(self):
        """Добавление ингредиента в заказ с поддержкой Firefox через JS drag_and_drop"""
        self.wait_for_element_to_be_clickable(MainPageLocators.BUN_INGREDIENT)
        
        # Определяем браузер
        browser_name = self.driver.capabilities.get('browserName', '').lower()
        
        if browser_name == 'firefox':
            # Для Firefox используем JS drag_and_drop
            self.drag_and_drop_js(MainPageLocators.BUN_INGREDIENT, MainPageLocators.ORDER_BASKET)
        else:
            # Для Chrome используем стандартный drag_and_drop
            try:
                self.drag_and_drop_on_element(MainPageLocators.BUN_INGREDIENT, MainPageLocators.ORDER_BASKET)
            except:
                # Если не работает, пробуем JS
                self.drag_and_drop_js(MainPageLocators.BUN_INGREDIENT, MainPageLocators.ORDER_BASKET)
        
        time.sleep(2)
    
    # МОДАЛЬНОЕ ОКНО ИНГРЕДИЕНТА
    def check_show_window_with_details(self):
        self.wait_until_element_visibility(MainPageLocators.INGREDIENT_DETAILS_POPUP)
        return self.get_actually_text(MainPageLocators.INGREDIENT_DETAILS_POPUP)
    
    def check_displayed_ingredient_details(self):
        return self.check_presense(MainPageLocators.INGREDIENT_DETAILS_POPUP).is_displayed()
    
    def invisibility_ingredient_details(self):
        self.check_invisibility(MainPageLocators.INGREDIENT_DETAILS_POPUP)
    
    # ЗАКАЗЫ
    def click_order_button(self):
        self.move_to_element_and_click(MainPageLocators.CREATE_ORDER_BUTTON)
    
    def click_close_modal_order(self):
        time.sleep(2)
        try:
            close_button = self.driver.find_element(*MainPageLocators.CLOSE_MODAL_ORDER)
            self.driver.execute_script("arguments[0].click();", close_button)
        except:
            try:
                close_button = self.driver.find_element(By.XPATH, "//div[contains(@class, 'Modal')]//button")
                self.driver.execute_script("arguments[0].click();", close_button)
            except:
                pass
        time.sleep(2)
    
    def check_show_window_with_order_id(self):
        self.wait_until_element_visibility(MainPageLocators.ORDER_IDENTIFICATE)
        return self.get_actually_text(MainPageLocators.ORDER_IDENTIFICATE)
    
    def get_with_order_id(self):
        self.wait_until_element_visibility(MainPageLocators.ORDER_ID)
        order_id = self.get_actually_text(MainPageLocators.ORDER_ID)
        while order_id == '9999':
            order_id = self.get_actually_text(MainPageLocators.ORDER_ID)
        return f"{order_id}"
    
    def check_displayed_order_status_text(self):
        return self.check_presense(MainPageLocators.ORDER_STATUS_TEXT).is_displayed()
    
    # ОБЩИЕ МЕТОДЫ
    def get_current_url(self):
        return self.driver.current_url
    
    def wait_for_url(self, expected_url):
        WebDriverWait(self.driver, TestData.WAIT_TIMEOUT).until(
            lambda driver: driver.current_url == expected_url
        )
    
    def click_order_history_button(self):
        self.click_on_element((By.XPATH, "//a[text()='История заказов']"))
    
    def is_order_id_found_at_history(self, order_number):
        try:
            elements = self.find_elements((By.XPATH, f"//div[contains(@class, 'OrderHistory_textBox')]//p[contains(text(), '{order_number}')]"))
            return len(elements) > 0
        except:
            return False
    
    def is_order_id_found_at_feed(self, order_number):
        try:
            elements = self.find_elements((By.XPATH, f"//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[contains(text(), '{order_number}')]"))
            return len(elements) > 0
        except:
            return False
    
    def get_user_order_in_progress(self):
        try:
            element = self.driver.find_element(*OrderFeedLocators.NUMBER_IN_PROGRESS)
            return element.text
        except:
            return ""