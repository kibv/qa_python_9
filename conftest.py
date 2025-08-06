import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.signup_page import SignupPage
from pages.signin_page import SigninPage
from data.data import URLs
from data.helpers import generate_credentials
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


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
