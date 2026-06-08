import pytest
import allure
from data import CourierData
from data import CourierResponse


@allure.title("Авторизация курьера")
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, courier, courier_methods):
        _, _, reg_data = courier
        status_code, courier_data, _ = courier_methods.authorize_courier(reg_data)
        assert (
            not isinstance(courier_data, str)
            and status_code == 200
            and len(courier_data) == 1
        ), f"{status_code}, message: {courier_data}"

    @allure.title("Ошибка при авторизации курьера при отправке неполных данных")
    @pytest.mark.parametrize(
        "params",
        [
            CourierData.COURIER_DATA_EMPTY_LOGIN_AND_PASSWORD,
            CourierData.COURIER_DATA_EMPTY_LOGIN,
            CourierData.COURIER_DATA_EMPTY_PASSWORD
        ],
    )
    def test_login_courier_witout_required_fields(self, params, courier_methods):
        status_code, courier_data, _ = courier_methods.authorize_courier(params)
        assert (
            not isinstance(courier_data, str)
            and status_code == 400
            and courier_data == CourierResponse.LOGIN_COURIER_RESPONSE_FAIL_400
        ), f"{status_code}, message: {courier_data}"
    
    @allure.title("Ошибка при авторизации незарегестрированного курьера или при невалидных логине и/или пароле")
    @pytest.mark.parametrize(
        "params",
        [
            CourierData.NO_REGISRETED_COURIER_DATA,
            CourierData.NO_VALID_PASSWORD_COURIER_DATA,
            CourierData.NO_VALID_LOGIN_COURIER_DATA
        ],
    )
    def test_login_courier_witout_registration(self, params, courier_methods):
        status_code, courier_data, _ = courier_methods.authorize_courier(params)
        assert (
            not isinstance(courier_data, str)
            and status_code == 404
            and courier_data == CourierResponse.LOGIN_COURIER_RESPONSE_FAIL_404
        ), f"{status_code}, message: {courier_data}"
