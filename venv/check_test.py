import requests
from configuration import BASE_URL, TRACK_PATH, ORDER_PATH
from data import payload

# Шаг 1. Выполняем запрос на создание заказа
create_order_url = BASE_URL + ORDER_PATH
response = requests.post(create_order_url, json=payload)
response_data = response.json()

# Шаг 2. Сохраняем номер трека заказа
order_track = response_data.get("track")

# Шаг 3. Выполняем запрос на получение заказа по треку заказа
get_order_url = BASE_URL + TRACK_PATH + f"{order_track}"
response = requests.get(get_order_url)
response_data = response.json()

# Шаг 4. Проверяем, что код ответа равен 200
assert response.status_code == 200

# Если все проверки прошли успешно, тест считается пройденным
print(response.status_code)