import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from data import TestData


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем ссылку')
    def open_link(self, url):
        return self.driver.get(url)

    @allure.step('Кликаем по элементу {locator}')
    def click_on_element(self, locator):
        try:
            WebDriverWait(self.driver, TestData.WAIT_TIMEOUT).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except ElementClickInterceptedException:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Вставить текст {text}')
    def set_text_to_element(self, locator, text):
        WebDriverWait(self.driver, TestData.WAIT_TIMEOUT).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получить текущий текст')
    def get_actually_text(self, locator):
        actually_text = self.driver.find_element(*locator).text
        return actually_text

    @allure.step('Проверить присутствие элемента на странице')
    def check_presense(self, locator):
        WebDriverWait(self.driver, TestData.WAIT_TIMEOUT).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Проверить невидимость элемента')
    def check_invisibility(self, locator):
        return WebDriverWait(self.driver, TestData.WAIT_TIMEOUT).until(EC.invisibility_of_element(locator))

    @allure.step('Дождаться видимости элемента')
    def wait_until_element_visibility(self, locator):
        return WebDriverWait(self.driver, TestData.WAIT_TIMEOUT).until(EC.visibility_of_element_located(locator))

    @allure.step('Дождаться невидимости элемента')
    def wait_until_element_invisible(self, locator):
        return WebDriverWait(self.driver, TestData.WAIT_TIMEOUT).until(EC.invisibility_of_element(locator))

    @allure.step('Получить текущую ссылку')
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step('Получить имя браузера')
    def get_browser_name(self):
        """Возвращает имя текущего браузера"""
        return self.driver.capabilities.get('browserName', '').lower()

    @allure.step('Перетащить элемент (стандартный)')
    def drag_and_drop_on_element(self, locator_one, locator_two):
        draggable = self.driver.find_element(*locator_one)
        droppable = self.driver.find_element(*locator_two)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()

    @allure.step('Перетащить элемент через JavaScript (для Firefox)')
    def drag_and_drop_js(self, source_locator, target_locator):
        self.wait_until_element_visibility(source_locator)
        self.wait_until_element_visibility(target_locator)

        element_from = self.driver.find_element(*source_locator)
        element_to = self.driver.find_element(*target_locator)

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)

    @allure.step('Переместиться до элемента и кликнуть')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step('Дождаться кликабельности элемента')
    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, TestData.WAIT_TIMEOUT).until(EC.element_to_be_clickable(locator))

    @allure.step('Найти элементы на странице')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Дождаться появления текста в элементе')
    def wait_for_text_to_be_present_in_element(self, locator, text):
        WebDriverWait(self.driver, TestData.WAIT_TIMEOUT).until(EC.text_to_be_present_in_element(locator, text))

    @allure.step("Нахождение нескольких элементов")
    def find_until_all_elements_located(self, locator):
        return WebDriverWait(self.driver, TestData.WAIT_TIMEOUT).until(EC.presence_of_all_elements_located(locator))