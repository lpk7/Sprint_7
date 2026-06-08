import pytest
import allure
from data import CourierData
from data import CourierResponse

@allure.title("Регистрация курьера")
class TestCreateCourier:

    @allure.title("Успешная регистрация нового курьера")
    def test_create_new_courier_success(self, courier_methods):
        status_code, courier_data = courier_methods.create_courier()
        assert (
            not isinstance(courier_data, str)
            and status_code == 201
            and courier_data == CourierResponse.CREATE_COURIER_RESPONSE_SUCCESS
        ), f"{status_code}, message: {courier_data}"

    @allure.title("Ошибка при регистрации существующего курьера")
    def test_create_couriers_with_same_data_fail(self, courier, courier_methods):
        _, _, reg_data = courier
        status_code, courier_data = courier_methods.create_courier(reg_data)
        assert (
            not isinstance(courier_data, str)
            and status_code == 409
            and courier_data == CourierResponse.CREATE_COURIER_RESPONSE_FAIL_409
        ), f"{status_code}, message: {courier_data}"

    @allure.title("Ошибка при регистрации курьера с отправкой неполных данных")
    @pytest.mark.parametrize(
        "params",
        [
            CourierData.COURIER_DATA_ONLY_FIRSTNAME,
            CourierData.COURIER_DATA_ONLY_LOGIN,
            CourierData.COURIER_DATA_ONLY_PASSWORD,
            CourierData.COURIER_DATA_WITHOUT_LOGIN,
            CourierData.COURIER_DATA_WITHOUT_PASSWORD,
        ],
    )
    def test_create_new_courier_witout_required_fields(self, params, courier_methods):
        status_code, courier_data = courier_methods.create_courier(params)
        assert (
            not isinstance(courier_data, str)
            and status_code == 400
            and courier_data == CourierResponse.CREATE_COURIER_RESPONSE_FAIL_400
        ), f"{status_code}, message: {courier_data}"
