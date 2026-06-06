import pytest
from methods.couriers_methods import CourierMethods
from methods.order_methods import OrderMethods
import data
import helpers


@pytest.fixture(scope="function")
def courier_methods(request):
    courier_methods = CourierMethods()
    return courier_methods

@pytest.fixture(scope="function")
def courier(courier_methods):
    reg_data = helpers.generate_new_courier()
    status_code, response_data = courier_methods.create_courier(reg_data)
    courier_id = courier_methods.authorize_courier(reg_data)
    print(courier_id)
    yield status_code, response_data, reg_data
    courier_methods.delete_courier(courier_id)

@pytest.fixture(scope="function")
def delete_courier_by_id(courier_methods):
    courier_id = courier_methods.authorize_courier(data.COURIER_DATA)
    courier_methods.delete_courier(courier_id)

@pytest.fixture(scope="function")
def order_methods():
    order_methods = OrderMethods()
    return order_methods


@pytest.fixture(scope="function")
def order_courier():
    return CourierMethods(url=f"", headers={})
