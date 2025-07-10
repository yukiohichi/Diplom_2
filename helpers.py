import time
from faker import Faker

faker = Faker()


def get_random_user():
    return {
        "email": f"{faker.user_name()}_{int(time.time() * 1000)}@gmail.com",
        "password": faker.password(),
        "name": f"{faker.user_name()}_{int(time.time() * 1000)}"
    }
