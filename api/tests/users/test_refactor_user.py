import pytest
import allure

from api.methods.users import UsersMethods

@allure.epic('Редактирование пользовательских данных')
class TestRefactorUser(UsersMethods):


    @allure.title('Редактирование пользовательских данных. Положительный')
    @pytest.mark.parametrize('data', [
        {'email': 'ayjcfgjfgvku009787v8@mail.com'},
        {'password': '111admin'},
        {'name': 'SayMyName'}
    ])
    def test_refactor_user_success(self, register_user, data):
        status, body = self.patch_data_user(register_user, data)

        assert status == 200 and body.get('success') is True


    @allure.title('Редактирование пользовательских данных. Негативный')
    @pytest.mark.parametrize('data', [
        {'email': 'fail@mail.com'},
        {'password': 'error'},
        {'name': 'error'}
    ])
    def test_refactor_user_no_auth(self, data):
        status, body = self.patch_data_user('', data)

        assert status == 401 and body.get('success') is False