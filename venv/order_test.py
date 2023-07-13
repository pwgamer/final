import requests
from configuration import BASE_URL, TRACK_PATH, ORDER_PATH
from data import payload

def test_order_creation_and_retrieval():
# Шаг 1: Выполняем запрос на создание заказа
    order_url = BASE_URL + ORDER_PATH
    response = requests.post(order_url, json=payload)
    response_data = response.json()

    assert "track" in response_data

# Шаг 2: Сохраняем номер трека заказа
    track = response_data["track"]

# Шаг 3: Выполняем запрос на получение заказа по треку заказа
    order_details_url = BASE_URL + TRACK_PATH + str(track)
    response = requests.get(order_details_url)
    response_data = response.json()

# Шаг 4: Проверяем, что код ответа равен 200
    assert response.status_code == 200