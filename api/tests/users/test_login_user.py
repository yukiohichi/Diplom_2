import pytest
import allure

from api.methods.users import UsersMethods
from data.users import base_login_user


@allure.epic('Авторизация пользователя')
class TestLoginUser(UsersMethods):

    @allure.title('Авторизация пользователя. Положительный')
    def test_login_user(self, logout_user):
        status, body = self.post_login_user(base_login_user)

        assert status == 200

        logout_user['access_token'] = body['accessToken']
        logout_user['refresh_token'] = body['refreshToken']


    @allure.title('Авторизация пользователя. Негативный')
    @pytest.mark.parametrize('field, wrong_value', [
        ('email', 'wrong@test.com'),
        ('password', 'wrong_password1')
    ])
    def test_login_user_invalid_fields(self, field, wrong_value):
        user_data = base_login_user.copy()
        user_data[field] = wrong_value

        status, body = self.post_login_user(user_data)

        assert status == 401 and body.get("success") is False
