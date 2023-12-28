import configuration
import requests
import data


# Создание новго заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)


# Получение номера заказа.
def get_track_number():
    track_num = str(response.json()['track'])
    return track_num


# Получение информации о заказе по его номеру, возвращает тело ответа.
def get_order(number):
    response_order = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO + number)
    return response_order


# Тест на проверку кода ответа.
def test_get_order():
    response_test = get_order(track_number)
    assert response_test.status_code == 200


response = post_new_order(data.order_body)
track_number = get_track_number()
