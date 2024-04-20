import requests

from PiterskiyDvish.settings import JWT_TOKEN
from piter.models import Beautiful


def get_and_parse_json(url):
    # Отправляем GET-запрос
    response = requests.get(url)

    # Проверяем статус ответа
    if response.status_code == 200:
        # Парсим JSON из ответа
        json_data = response.json()
        return json_data
    else:
        print(f'Ошибка: {response.status_code}')
        return None


# Пример использования

def save_json_to_db(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        results = json_data.get('results', [])
        for item in results:
            my_model = Beautiful(
                oid=item['oid'],
                name=item['name'],
                name_en=item['name_en'],
                address_manual=item['address_manual'],
                phone=item['phone'],
                www=item['www'],
                email=item['email'],
                kitchen=item.get('kitchen', False),
                for_disabled=item.get('for_disabled', False),
                coord=item['coord']
            )
            my_model.save()
    else:
        print(f"Ошибка при получении данных: {response.status_code}")

url = 'https://spb-classif.gate.petersburg.ru/api/v2/datasets/143/versions/latest/data/570/'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {JWT_TOKEN}'
}
save_json_to_db(url, headers)
# url = 'https://spb-classif.gate.petersburg.ru/api/v2/datasets/143/versions/latest/data/570/'
# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': f'Bearer {JWT_TOKEN}'
# }
#
# response = requests.get(url, headers=headers)
# json_response = response.json()
#
# count = json_response['count']
# results = json_response['results']
#
# for item in results:
#     my_model = Beautiful(
#         oid=item['oid'],
#         name=item['name'],
#         name_en=item['name_en'],
#         address_manual=item['address_manual'],
#         phone=item['phone'],
#         www=item['www'],
#         email=item['email'],
#         kitchen=item.get('kitchen'),
#         for_disabled=item['for_disabled'],
#         coord=item['coord']
#     )
#     my_model.save()