
class OrderData:
    
    ORDER_DATA = {
        "firstName": "Сергей",
        "lastName": "Петров",
        "address": "Москва, ул. Шарикоподшипниковская, д. 4",
        "metroStation": "Сокольники",
        "phone": "+7 926 355 35 35",
        "rentTime": 2,
        "deliveryDate": "2026-06-06",
        "comment": "Видели ночь, гуляли всю ночь до утра"
    }
    COLOR = [
        {"color": ["BLACK"]},
        {"color": ["GREY"]},
        {"color": ["BLACK", "GREY"]},
        {"color": []}
    ]


class CourierResponse:

    CREATE_COURIER_RESPONSE_FAIL_409 = {
        "code": 409,
        "message": "Этот логин уже используется. Попробуйте другой.",
    }

    CREATE_COURIER_RESPONSE_SUCCESS = {"ok": True}

    CREATE_COURIER_RESPONSE_FAIL_400 = {
        "code": 400,
        "message": "Недостаточно данных для создания учетной записи",
    }

    LOGIN_COURIER_RESPONSE_FAIL_404 = {
        "code": 404,
        "message": "Учетная запись не найдена"
    }

    LOGIN_COURIER_RESPONSE_FAIL_400 = {
        "code": 400,
        "message":  "Недостаточно данных для входа"
    }


class CourierData:

    NEW_COURIER_DATA = {"login": "kurvabober", "password": "12345", "firstName": "kurvabober"}

    COURIER_DATA_ONLY_LOGIN = {"login": "kurvabober2"}

    COURIER_DATA_ONLY_PASSWORD = {"password": "12345"}

    COURIER_DATA_ONLY_FIRSTNAME = {"firstName": "kurvabober3"}

    NO_REGISRETED_COURIER_DATA = {"login": "kurvabober3", "password": "123458", "firstName": "kurvabober2"}

    NO_VALID_PASSWORD_COURIER_DATA = {
        "login": "ninja56",
        "password": "1234567"
    }
    NO_VALID_LOGIN_COURIER_DATA = {
        "login": "ninja567",
        "password": "123456"
    }

    COURIER_DATA_WITHOUT_LOGIN = {"password": "12345", "firstName": "kurvabober2"}

    COURIER_DATA_WITHOUT_PASSWORD = {"login": "kurvabober", "firstName": "kurvabober2"}

    COURIER_DATA_EMPTY_LOGIN_AND_PASSWORD = {
        "login": "",
        "password": ""
    }

    COURIER_DATA_EMPTY_LOGIN = {
        "login": "",
        "password": "12345"
    }

    COURIER_DATA_EMPTY_PASSWORD = {
        "login": "kurvabober3",
        "password": ""
    }
