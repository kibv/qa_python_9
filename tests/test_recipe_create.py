import allure
from pages.signin_page import SigninPage
from pages.recipe_create_page import RecipeCreatePage
from data.data import URLs, RECIPE_DATA


@allure.title("Проверка создания рецепта и отображения на главной странице")
class TestRecipe:
    @allure.story("Проверка рецепта")
    def test_create_recipe(self, browser, authorized_user):
        create_page = RecipeCreatePage(browser)
        login = SigninPage(browser)

        with allure.step("Переход на страницу создания рецепта"):
            # create_page.open(URLs.RECIPES_URL)
            create_page.go_create_recipe()
            create_page.wait_for_url_change(URLs.CREATE_URL)
            current_url = browser.current_url
            assert current_url == URLs.CREATE_URL, f"Открыт неверный URL: {current_url}"

        with allure.step("Создание рецепта"):
            name = RECIPE_DATA["name"]
            create_page.fill_recipe_form(
                name,
                description=RECIPE_DATA["description"],
                time=RECIPE_DATA["time"],
                ingredients=RECIPE_DATA["ingredients"],
                amount=RECIPE_DATA["amount"],
                patch_image=RECIPE_DATA["patch_image"]
            )
            login.open(URLs.BASE_URL)
            assert login.check_elem_logout(), "Кнопка выхода не отображается"

            assert create_page.is_recipe_card_displayed(name), \
                f"Карточка {name} рецепта не найдена на странице"

        # with allure.step("Выход"):
        #     create_page.open(URLs.RECIPES_URL)
        #     # create_page.go_logout()
        #     login.wait_for_url_change(URLs.RECIPES_URL)
        #     current_url = browser.current_url
        #     assert current_url == URLs.RECIPES_URL, f"Открыт неверный URL: {current_url}"
            create_page.go_logout()
