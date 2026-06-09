import pytest
from methods.couriers_methods import CourierMethods
from methods.order_methods import OrderMethods
from data import CourierData
import helpers


@pytest.fixture(scope="function")
def courier_methods(request):
    courier_methods = CourierMethods()
    return courier_methods

@pytest.fixture(scope="function")
def courier(courier_methods):
    params = helpers.generate_new_courier()
    yield params
    courier_id = courier_methods.authorize_courier(params)
    courier_methods.delete_courier(params)

@pytest.fixture(scope="function")
def order_methods():
    order_methods = OrderMethods()
    return order_methods
