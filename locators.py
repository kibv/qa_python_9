from selenium.webdriver.common.by import By


class SignupLocators:
    FIRST_NAME = (By.XPATH, "//input[@name='first_name']")
    LAST_NAME = (By.XPATH, "//input[@name='last_name']")
    USERNAME = (By.XPATH, "//input[@name='username']")
    EMAIL = (By.XPATH, "//input[@name='email']")
    PASSWORD = (By.XPATH, "//input[@name='password']")
    SUBMIT = (By.XPATH, "//button[text()='Создать аккаунт']")
    LOGOUT_BUTTON = (By.XPATH, "//a[@class='styles_menuLink__3a59I' and text()='Выход']")


class LoginLocators:
    EMAIL = (By.XPATH, "//input[@name='email']")
    PASSWORD = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_BUTTON = (By.LINK_TEXT, "Создать аккаунт")
    LOGIN_BUTTON = (By.LINK_TEXT, "Войти")
    ALERT_LOC = (By.CLASS_NAME, "styles_module__error__V_Ub0")
    LOGOUT_BUTTON = (By.XPATH, "//a[@class='styles_menuLink__3a59I' and text()='Выход']")
    LOGIN_ERROR_ALERT = (By.CLASS_NAME, "styles_module__error__3uLQ8")


class MainPageLocators:
    CREATE_BUTTON = (By.XPATH, "//a[@href='/recipes/create' and text()='Создать рецепт']")
    RECIPE_CARDS = (By.CLASS_NAME, "card")
    FAVORITE_BUTTON = (By.CLASS_NAME, "card__favorite")
    PURCHASE_BUTTON = (By.CLASS_NAME, "card__shopping-cart")


class RecipeCreateLocators:
    RECIPE_BUTTON = (By.XPATH, "//a[@href='/recipes' and text()='Рецепты']")
    CREATE_BUTTON_MAIN = (By.XPATH, "//a[@href='/recipes/create' and text()='Создать рецепт']")
    NAME_INPUT = (By.XPATH, "//div[text()='Название рецепта']/following-sibling::input")
    TAG_BUTTONS = (By.XPATH, "//div[text()='Теги']/following-sibling::div//button")
    INGREDIENT_NAME_INPUT = (By.XPATH, "//div[text()='Ингредиенты']/following-sibling::input")
    INGREDIENT_AMOUNT_INPUT = (By.XPATH, "//input[contains(@class, 'ingredientsAmountValue')]")
    DROPDOWN_INGREDIENT = (By.XPATH, "//div[@class='styles_container__3ukwm']/div[text()='раки']")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[text()='Добавить ингредиент']")
    COOKING_TIME_INPUT = (By.XPATH, "//div[text()='Время приготовления']/following-sibling::input")
    DESCRIPTION_INPUT = (By.XPATH, "//div[text()='Описание рецепта']/following-sibling::textarea")
    PHOTO_UPLOAD_INPUT = (By.XPATH, "//input[@type='file']")
    CREATE_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать рецепт')]")
    RECIPE_CARD_TITLE = (By.CLASS_NAME, "card__title")
    LOGOUT_BUTTON = (By.XPATH, "//a[@class='styles_menuLink__3a59I' and text()='Выход']")
    @staticmethod
    def recipe_card_by_name(name: str):
        return By.XPATH, f"//div[contains(@class, 'style_card__1Le2w')]//a[contains(text(), '{name}')]"
