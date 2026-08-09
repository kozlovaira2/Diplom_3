import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from data import TestData


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    driver.get(TestData.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def pages(driver):
    from pages.main_page import MainPage
    return MainPage(driver)


@pytest.fixture
def login(driver, pages):
    from helpers import login_registered_user
    login_registered_user(driver)
    return pages