import allure
from pages.signin_page import SigninPage
from pages.recipe_create_page import RecipeCreatePage
from data.data import URLs, RECIPE_DATA_SETS
from data.helpers import generate_recipe_data


@allure.title("Проверка создания рецепта и отображения на главной странице")
class TestRecipe:
    @allure.story("Проверка рецепта")
    def test_create_recipe(self, browser, authorized_user):
        create_page = RecipeCreatePage(browser)
        login = SigninPage(browser)

        with allure.step("Переход на страницу создания рецепта"):
            create_page.go_create_recipe()
            create_page.wait_for_url_change(URLs.CREATE_URL)
            current_url = browser.current_url
            assert current_url == URLs.CREATE_URL, f"Открыт неверный URL: {current_url}"

        with allure.step("Создание рецепта"):
            recipe_data = generate_recipe_data(RECIPE_DATA_SETS)
            name = recipe_data["name"]
            description = recipe_data["description"],
            time = recipe_data["time"],
            ingredients = recipe_data["ingredients"],
            amount = recipe_data["amount"],
            patch_image = recipe_data["patch_image"]
            create_page.fill_recipe_form(name, description, time, amount, ingredients, patch_image)
            login.open(URLs.BASE_URL)
            assert login.check_elem_logout(), "Кнопка выхода не отображается"

            assert create_page.is_recipe_card_displayed(name), \
                f"Карточка {name} рецепта не найдена на странице"

        with allure.step("Выход"):
            create_page.go_logout()
            login.wait_for_url_change(URLs.RECIPES_URL)
            current_url = browser.current_url
            assert current_url == URLs.RECIPES_URL, f"Открыт неверный URL: {current_url}"
