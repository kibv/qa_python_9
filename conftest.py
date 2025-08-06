import pytest
import pytest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.signup_page import SignupPage
from pages.signin_page import SigninPage
from data.data import URLs
from data.helpers import generate_credentials
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.browser_version = "128.0"  # Указываем версию из browsers.json
    chrome_options.set_capability("enableVNC", True)  # Опционально для Selenoid
    chrome_options.set_capability("enableVideo", False)  # Опционально

    driver = webdriver.Remote(
        command_executor='http://selenoid:4444/wd/hub',
        options=chrome_options
    )
    yield driver
    driver.quit()
#
# @pytest.fixture(scope="function")
# def browser():
#     options = Options()
#     options.add_argument("--headless=new")
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     options.add_argument("--window-size=1920,1080")
#     yield driver
#     driver.quit()


@pytest.fixture(scope="function")
def registered_user(browser):
    name, lastname, username, email, password = generate_credentials()
    browser.get(URLs.REGISTER_URL)
    auth_page = SignupPage(browser)
    auth_page.register(name, lastname, username, email, password)
    return {
        "name": name,
        "lastname": lastname,
        "username": username,
        "email": email,
        "password": password
    }


@pytest.fixture()
def authorized_user(browser, registered_user):
    browser.get(URLs.LOGIN_URL)
    auth_page = SigninPage(browser)
    auth_page.login(registered_user["email"], registered_user["password"])
    return registered_user
