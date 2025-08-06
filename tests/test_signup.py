import allure
from pages.signup_page import SignupPage
from data.data import URLs

@allure.title("Регистрация пользователя")
class TestSignup:
    @allure.story("Проверка кнопки и регистрация")
    def test_registration(self, browser):
        register = SignupPage(browser)
        with allure.step("Проверка формы авторизации и URL"):
            # register.wait_for_url_change(URLs.REGISTER_URL)
            # import time
            # time.sleep(5)
            register.wait_for_url_change(URLs.LOGIN_URL)
            current_url = browser.current_url
            assert register.check_elem(), "Форма не отображается"
            assert current_url == URLs.LOGIN_URL, f"Открыт неверный URL: {current_url}"
            # register.go_logout()
