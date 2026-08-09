from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDERS_LIST_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')
    ORDER_STRUCTURE = (By.XPATH, '//p[text()="Cостав"]')
    ORDER_LINK = (By.XPATH, '//*[contains(@class, "OrderHistory_link")]')
    
    TOTAL_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DAILY_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    NUMBER_IN_PROGRESS = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")
    
    ALL_ORDERS_AT_FEED = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text text_type_digits-default']")