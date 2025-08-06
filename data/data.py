import random
from pathlib import Path
from data.helpers import get_random_number


class URLs:
    BASE_URL = "https://foodgram-frontend-1.prakticum-team.ru/"
    REGISTER_URL = BASE_URL + "signup"
    LOGIN_URL = BASE_URL + "signin"
    RECIPES_URL = BASE_URL + "recipes"
    CREATE_URL = BASE_URL + "recipes/create"
    SUB_URL = BASE_URL + "subscriptions"
    FAVORITES_URL = BASE_URL + "favorites"
    CART_URL = BASE_URL + "cart"
    RESET_PASSWORD_URL = BASE_URL + "change-password"


RECIPE_DATA_SETS = [
    {
        "name": f"Кротовуха натуральная {get_random_number()}",
        "ingredients": "раки",
        "tag": random.choice(["Завтрак", "Обед", "Ужин"]),
        "description": "Классическая кротовуха",
        "time": "15",
        "amount": "12",
        "patch_image": str(Path("data/images/test_image1.png").resolve())
    },
    {
        "name": f"Борщ фруктовый {get_random_number()}",
        "ingredients": "раки",
        "tag": random.choice(["Завтрак", "Обед", "Ужин"]),
        "description": "Пряный салат для любителей острых вкусов",
        "time": "20",
        "amount": "10",
        "patch_image": str(Path("data/images/test_image2.png").resolve())
    },
    {
        "name": f"Окрошка на миндальном молоке с раками {get_random_number()}",
        "ingredients": "раки",
        "tag": random.choice(["Завтрак", "Обед", "Ужин"]),
        "description": "Классический рецепт с нежным вкусом",
        "time": "10",
        "amount": "15",
        "patch_image": str(Path("data/images/test_image3.png").resolve())
    }
]

