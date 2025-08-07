import allure
from pages.signin_page import SigninPage
from data.data import URLs


@allure.title("Авторизация")
class TestSignin:
    @allure.story("Проверка Авторизации")
    def test_autorizacion(self, browser, authorized_user):
        with allure.step("Проверка авторизации"):
            login = SigninPage(browser)
            login.wait_for_url_change(URLs.RECIPES_URL)
            current_url = browser.current_url
            assert current_url == URLs.RECIPES_URL, f"Открыт неверный URL: {current_url}"

        with allure.step("Проверка кнопки выхода"):
            login.open(URLs.BASE_URL)
            assert login.check_elem_logout(), "Кнопка выхода не отображается"

        with allure.step("Проверка кнопки выхода"):
            login.open(URLs.BASE_URL)
            assert login.check_elem_logout(), "Кнопка выхода не отображается"
