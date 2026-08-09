from selenium.webdriver.common.by import By


class MainPageLocators:
    # НАВИГАЦИЯ - из вашего рабочего кода
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]/parent::a')
    ORDERS_LIST_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')  # ЗАГЛАВНАЯ "З"
    LOGIN_BUTTON_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    PROFILE_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
    MAIN_LIST_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    
    # ИНГРЕДИЕНТЫ - из вашего рабочего кода
    BUN_INGREDIENT = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')
    INGREDIENT_DETAILS_POPUP = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    CROSS_BUTTON = (By.XPATH, '//button[contains(@class,"close")]')
    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')
    ORDER_BASKET = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (низ)']")
    
    # ЗАКАЗЫ - из вашего рабочего кода
    CREATE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    CLOSE_MODAL_ORDER = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]")
    ORDER_IDENTIFICATE = (By.XPATH, '//p[text()="идентификатор заказа"]')
    ORDER_ID = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
    ORDER_STATUS_TEXT = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')