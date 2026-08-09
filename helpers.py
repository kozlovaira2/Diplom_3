from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from data import TestData


def login_registered_user(driver):
    # Клик по кнопке "Войти в аккаунт"
    driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
    
    # Ввод email
    WebDriverWait(driver, TestData.WAIT_TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']"))
    )
    driver.find_element(By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']").send_keys(TestData.REGISTERED_EMAIL)
    
    # Ввод пароля
    driver.find_element(By.XPATH, ".//input[@type='password' and @name='Пароль']").send_keys(TestData.REGISTERED_PASSWORD)
    
    # Клик по кнопке "Войти"
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    
    # Ждем загрузки главной страницы
    WebDriverWait(driver, TestData.WAIT_TIMEOUT).until(
        EC.presence_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON)
    )