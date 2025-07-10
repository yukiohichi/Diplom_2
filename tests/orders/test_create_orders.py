import allure
import pytest

from methods_api.orders import OrderMethods
from data.orders import order_ingredients, order_ingredients_zero, order_ingredients_incorrect

@allure.epic('Создание заказа')
class TestCreateOrders(OrderMethods):

    #с авторизацией, с ингредиентами
    @allure.title('Создание заказа с авторизацией, с ингредиентами. Положительный')
    def test_create_orders_success(self, register_user):
        status, body = self.post_create_order(register_user, order_ingredients)

        assert status == 200 and body.get('success') is True

    #без авторизации, с ингредиентами
    @allure.title('Создание заказа без авторизации, с ингредиентами. Положительный')
    def test_create_orders_no_auth(self):
        status, body = self.post_create_order('', order_ingredients)

        assert status == 200 and body.get('success') is True

    #с авторизацией, без ингредиентов
    @allure.title('Создание заказа с авторизацией, без ингредиентов. Негативный')
    def test_create_order_no_ingredients(self, register_user):
        status, body = self.post_create_order(register_user, order_ingredients_zero)

        assert status == 500 and ("Internal Server Error" in body or "error" in body.lower()), \
            f"Ожидался статус 500 и сообщение об ошибке, получено: статус={status}, тело={body}"

    #В реальном проекте на 500 тесты не пишут
    @allure.title('Создание заказа без авторизации, без ингредиентов. Негативный')
    def test_create_order_no_auth_no_ingredients(self):
        status, body = self.post_create_order('', order_ingredients_zero)

        assert status == 500 and ("Internal Server Error" in body or "error" in body.lower()), \
            f"Ожидался статус 500 и сообщение об ошибке, получено: статус={status}, тело={body}"


    #В реальном проекте на 500 тесты не пишут
    @allure.title('Создание заказа с авторизацией, с неверным хэшем ингредиентов. Негативный')
    def test_create_order_incorrect_ingredients(self, register_user):
        status, body = self.post_create_order(register_user, order_ingredients_incorrect)
        assert status == 400 and body.get('success') is False