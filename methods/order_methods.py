import allure
import requests
import json
import urls


class OrderMethods:

    @allure.step("Создание заказа")
    def create_order(self, params):
        response = requests.post(f"{urls.BASE_URL}{urls.ORDERS_URL}", json=params)
        try:
            return response.status_code, response.json()
        except json.JSONDecodeError:
            return response.status_code, response.text
        
    @allure.step("Получение списка заказов")
    def order_list(self):
        response = requests.get(f"{urls.BASE_URL}{urls.ORDERS_URL}")
        try:
            return response.status_code, response.json()
        except json.JSONDecodeError:
            return response.status_code, response.text