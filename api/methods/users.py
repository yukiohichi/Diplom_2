import json
import requests
import allure
from data.urls import BASE_URL, AUTH_URL

class UsersMethods:

    #создание пользователя
    @allure.step('Регистрация пользователя')
    def post_register_user(self, params):
        response = requests.post(
            f'{BASE_URL}{AUTH_URL}register', json=params
        )
        try:
            return response.status_code, response.json()
        except json.JSONDecodeError:
            return response.status_code, response.text

    #логин пользователя
    @allure.step('Авторизация пользователя')
    def post_login_user(self, params):

        response = requests.post(f'{BASE_URL}{AUTH_URL}login', json=params)
        try:
            return response.status_code, response.json()

        except json.JSONDecodeError:
            return response.status_code, response.text

    #изменение данных о пользователе
    @allure.step('Изменение данных о пользователе')
    def patch_data_user(self, access_token,params):
        headers = {
            'Authorization': access_token,
            'Content-Type': 'application/json'
        }
        response = requests.patch(
            f'{BASE_URL}{AUTH_URL}user', headers=headers, json=params)
        try:
            return response.status_code, response.json()
        except json.JSONDecodeError:
            return response.status_code, response.text

    # удаление пользователя
    @allure.step('Удаление пользователя')
    def delete_user(self, access_token):
        headers = {
            'Authorization': access_token,
            'Content-Type': 'application/json'
        }
        response = requests.delete(f'{BASE_URL}{AUTH_URL}user', headers=headers)
        try:
            return response.status_code, response.json()

        except json.JSONDecodeError:
            return response.status_code, response.text

    # получение данных о пользователе
    @allure.step('Получение данных о пользователе')
    def get_user(self, access_token):
        headers = {
            'Authorization': access_token,
            'Content-Type': 'application/json'
        }
        response = requests.get(f'{BASE_URL}{AUTH_URL}user', headers=headers)
        try:
            return response.status_code, response.json()

        except json.JSONDecodeError:
            return response.status_code, response.text

    #выход из системы
    @allure.step('Выход пользователя из системы')
    def post_logout_user(self, access_token, refresh_token):
        headers = {
            'Authorization': access_token,
            'Content-Type': 'application/json'
        }
        data = {
            'token': refresh_token
        }
        response = requests.post(f'{BASE_URL}{AUTH_URL}logout', headers=headers, json=data)
        try:
            return response.status_code, response.json()

        except json.JSONDecodeError:
            return response.status_code, response.text
