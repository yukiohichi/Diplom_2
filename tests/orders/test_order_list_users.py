import allure
import pytest

from methods_api.orders import OrderMethods

@allure.epic('Список заказов пользователя')
class TestOrderUsers(OrderMethods):

    @allure.title('Запрос на список заказов пользователя. Положительный')
    def test_order_user_success(self, register_user):
        status, body = self.get_order_user(register_user)
        assert status == 200 and body.get('success') is True

    @allure.title('Запрос на список заказов пользователя. Негативный')
    def test_order_user_no_auth(self):
        status, body = self.get_order_user('')
        assert status == 401 and body.get('success') is False