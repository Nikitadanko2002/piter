import io
import sys

from django.shortcuts import render

from django.http import JsonResponse
import requests

from PiterskiyDvish.settings import JWT_TOKEN
from .models import KudaGoCategories, Beautiful


def fetch_and_save_data(request):
    if request.method == 'GET':
        # URL внешнего API
        url = 'https://spb-afisha.gate.petersburg.ru/kg/external/afisha/categories'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {JWT_TOKEN}'
        }
        response = requests.get(url, headers=headers)
        json_response = response.json()
        # Проверка успешности запроса
        if response.status_code == 200:
            data = response.json()

            # Сохранение данных в модель
            for item in data['data']:
                KudaGoCategories.objects.create(
                    name=item['name'],
                    id=item['id'],
                    slug=item['slug']
                )


import requests


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def makebeautiful():
    url = 'https://spb-classif.gate.petersburg.ru/api/v2/datasets/143/versions/latest/data/570/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {JWT_TOKEN}'
    }

    response = requests.get(url, headers=headers)
    json_response = response.json()
    print(json_response)
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
makebeautiful()


