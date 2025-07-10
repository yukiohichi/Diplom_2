import json
import requests
import allure
from data.urls import BASE_URL, ORDER_URL

class OrderMethods:

    @allure.step('Создание заказа')
    def post_create_order(self, access_token, params):
        headers = {
            'Authorization': access_token,
            'Content-Type': 'application/json'
        }
        response = requests.post(
            f'{BASE_URL}{ORDER_URL}', headers=headers, json=params)
        try:
            return response.status_code, response.json()
        except json.JSONDecodeError:
            return response.status_code, response.text

    @allure.step('Получение списка заказов')
    def get_order_user(self, access_token):
        headers = {
            'Authorization': access_token,
            'Content-Type': 'application/json'
        }
        response = requests.get(f'{BASE_URL}{ORDER_URL}', headers=headers)
        try:
            return response.status_code, response.json()

        except json.JSONDecodeError:
            return response.status_code, response.text
