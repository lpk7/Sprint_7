import pytest
import allure
from data import OrderData

class TestOrder:

    @allure.title("Создание заказа")
    @pytest.mark.parametrize("payload_override", OrderData.COLOR)
    def test_create_order_success(self, order_methods, payload_override):
        order_payload = {**OrderData.ORDER_DATA, **payload_override}
        status_code, response = order_methods.create_order(order_payload)
        assert (
            not isinstance(response, str)
            and status_code == 201
            and "track" in response
        ), f"{status_code}, message: {response}"

    @allure.title("Получение списка заказов")
    def test_order_list(self, order_methods):
        status_code, response = order_methods.order_list()
        assert (
            not isinstance(response, str)
            and status_code == 200
            and "orders" in response
        ), f"{status_code}, message: {response}"