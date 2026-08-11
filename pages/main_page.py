from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators
from selenium.webdriver.common.by import By
from data import TestData
import allure


class MainPage(BasePage):
    
    # НАВИГАЦИЯ
    @allure.step('Клик по кнопке "Лента заказов"')
    def click_orders_list_button(self):
        self.click_on_element(MainPageLocators.ORDERS_LIST_BUTTON)
        self.wait_until_element_visibility(OrderFeedLocators.ORDERS_LIST_TITLE)
    
    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_until_element_visibility(MainPageLocators.MAIN_LIST_TITLE)
    
    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_on_account(self):
        self.click_on_element(MainPageLocators.PROFILE_BUTTON)
    
    @allure.step('Клик по кнопке "Войти в аккаунт"')
    def click_login_button(self):
        self.click_on_element(MainPageLocators.LOGIN_BUTTON_MAIN)
    
    # ИНГРЕДИЕНТЫ
    @allure.step('Клик на ингредиент')
    def click_on_ingredient(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.BUN_INGREDIENT)
        self.click_on_element(MainPageLocators.BUN_INGREDIENT)
    
    @allure.step('Клик по крестику для закрытия модального окна')
    def click_cross_button(self):
        self.move_to_element_and_click(MainPageLocators.CROSS_BUTTON)
    
    @allure.step('Получение значения счетчика ингредиента')
    def get_count_value(self):
        try:
            self.wait_until_element_visibility(MainPageLocators.INGREDIENT_COUNTER)
            return self.get_actually_text(MainPageLocators.INGREDIENT_COUNTER)
        except:
            return 0
    
    @allure.step('Добавление ингредиента в заказ')
    def add_filling_to_order(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.BUN_INGREDIENT)
        
        if self.get_browser_name() == 'firefox':
            self.drag_and_drop_js(MainPageLocators.BUN_INGREDIENT, MainPageLocators.ORDER_BASKET)
        else:
            try:
                self.drag_and_drop_on_element(MainPageLocators.BUN_INGREDIENT, MainPageLocators.ORDER_BASKET)
            except:
                self.drag_and_drop_js(MainPageLocators.BUN_INGREDIENT, MainPageLocators.ORDER_BASKET)
        
        self.wait_until_element_visibility(MainPageLocators.INGREDIENT_COUNTER)
    
    # МОДАЛЬНОЕ ОКНО ИНГРЕДИЕНТА
    @allure.step('Проверка появления окна с деталями ингредиента')
    def check_show_window_with_details(self):
        self.wait_until_element_visibility(MainPageLocators.INGREDIENT_DETAILS_POPUP)
        return self.get_actually_text(MainPageLocators.INGREDIENT_DETAILS_POPUP)
    
    @allure.step('Проверка видимости окна с деталями ингредиента')
    def check_displayed_ingredient_details(self):
        return self.check_presense(MainPageLocators.INGREDIENT_DETAILS_POPUP).is_displayed()
    
    @allure.step('Проверка невидимости окна с деталями ингредиента')
    def invisibility_ingredient_details(self):
        self.check_invisibility(MainPageLocators.INGREDIENT_DETAILS_POPUP)
    
    # ЗАКАЗЫ
    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_order_button(self):
        self.move_to_element_and_click(MainPageLocators.CREATE_ORDER_BUTTON)
        self.wait_until_element_visibility(MainPageLocators.ORDER_IDENTIFICATE)
    
    @allure.step('Закрытие модального окна с заказом')
    def click_close_modal_order(self):
        self.wait_until_element_visibility(MainPageLocators.CLOSE_MODAL_ORDER)
        self.click_on_element(MainPageLocators.CLOSE_MODAL_ORDER)
        self.wait_until_element_invisible(MainPageLocators.CLOSE_MODAL_ORDER)
    
    @allure.step('Проверка появления окна с идентификатором заказа')
    def check_show_window_with_order_id(self):
        self.wait_until_element_visibility(MainPageLocators.ORDER_IDENTIFICATE)
        return self.get_actually_text(MainPageLocators.ORDER_IDENTIFICATE)
    
    @allure.step('Получение номера заказа из модального окна')
    def get_with_order_id(self):
        self.wait_until_element_visibility(MainPageLocators.ORDER_ID)
        order_id = self.get_actually_text(MainPageLocators.ORDER_ID)
        self.wait_until_text_not_equal(MainPageLocators.ORDER_ID, '9999')
        return self.get_actually_text(MainPageLocators.ORDER_ID)
    
    @allure.step('Проверка статуса заказа "Ваш заказ начали готовить"')
    def check_displayed_order_status_text(self):
        return self.check_presense(MainPageLocators.ORDER_STATUS_TEXT).is_displayed()
    
    # ОБЩИЕ МЕТОДЫ
    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return super().get_current_url()
    
    @allure.step('Ожидание перехода по URL')
    def wait_for_url(self, expected_url):
        self.wait_until_url_equals(expected_url)
    
    @allure.step('Клик по кнопке "История заказов"')
    def click_order_history_button(self):
        self.click_on_element((By.XPATH, "//a[text()='История заказов']"))
    
    @allure.step('Проверка наличия заказа в истории')
    def is_order_id_found_at_history(self, order_number):
        try:
            elements = self.find_elements((By.XPATH, f"//div[contains(@class, 'OrderHistory_textBox')]//p[contains(text(), '{order_number}')]"))
            return len(elements) > 0
        except:
            return False
    
    @allure.step('Проверка наличия заказа в ленте')
    def is_order_id_found_at_feed(self, order_number):
        try:
            elements = self.find_elements((By.XPATH, f"//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[contains(text(), '{order_number}')]"))
            return len(elements) > 0
        except:
            return False
    
    @allure.step('Получение номера заказа в разделе "В работе"')
    def get_user_order_in_progress(self):
        try:
            self.wait_until_element_visibility(OrderFeedLocators.NUMBER_IN_PROGRESS)
            return self.get_actually_text(OrderFeedLocators.NUMBER_IN_PROGRESS)
        except:
            return ""