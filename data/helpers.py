import random
import uuid

def get_random_number():
    return str(random.randint(10000000, 90000000))

def generate_credentials():
    password = f"fsZ{str(uuid.uuid4())[:-30]}{get_random_number()}"
    name = f'Шеф{get_random_number()}'
    lastname = f'Шефский{get_random_number()}'
    username = f'test{get_random_number()}'
    email = f"{get_random_number()}@yandex.ru"
    return name, lastname, username, email, password
