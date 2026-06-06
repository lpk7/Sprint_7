import data
import allure
import requests
import helpers
import json
import urls


class CourierMethods:
    
    @allure.step("Регистрация курьера")
    def create_courier(self, params=None):
        if params is None:
            params = helpers.generate_new_courier()
        response = requests.post(f"{urls.BASE_URL}{urls.COURIERS_URL}", data=params)
        try:
            return response.status_code, response.json()
        except json.decoder.JSONDecodeError:
            return response.status_code, response.text

    @allure.step("Авторизация курьера")
    def authorize_courier(self, params):
        response = requests.post(
            f"{urls.BASE_URL}{urls.COURIERS_URL}login", data=params
        )
        try:
            data = response.json()
            courier_id = data.get("id")
            return response.status_code, data, courier_id
        except json.decoder.JSONDecodeError:
            return response.status_code, response.text

    @allure.step("Удаление курьера")
    def delete_courier(self, courier_id):
        response = requests.delete(f"{urls.BASE_URL}{urls.COURIERS_URL}{courier_id}")
        try:
            return response.status_code, response.json()
        except json.decoder.JSONDecodeError:
            return response.status_code, response.text
