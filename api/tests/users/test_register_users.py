import pytest
import allure

from api.methods.users import UsersMethods
from data.users import base_register_user
from helpers import get_random_user


@allure.epic('Регистрация пользователя')
class TestRegisterUsers(UsersMethods):

    @allure.title('Регистрация нового пользователя. Положительный')
    def test_register_user_success(self, cleanup_user):
        status, body = self.post_register_user(get_random_user())

        assert status == 200 and body.get('success') is True

        cleanup_user['token'] = body.get('accessToken')

    @allure.title('Регистрация пользователя с дублирующими данными. Негативный ')
    def test_register_duplicate_user(self, cleanup_user):
        status, body = self.post_register_user(base_register_user)

        assert status == 403 and body.get('success') is False


    @allure.title('Регистрация пользователя с пропущенным обязательным полем. Негативный')
    @pytest.mark.parametrize('missing_field', ['email', 'password', 'name'])
    def test_register_user_missing_field(self, missing_field):
        user_data = get_random_user()
        user_data.pop(missing_field)

        status, body = self.post_register_user(user_data)

        assert status == 403 and body.get('success') is False
