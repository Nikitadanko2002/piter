import json

from django.shortcuts import HttpResponse

from PiterskiyDvish.settings import JWT_TOKEN

import requests

from django.shortcuts import render
import requests

def import_data_from_url(request):
    url = 'https://spb-afisha.gate.petersburg.ru/kg/external/afisha/categories'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {JWT_TOKEN}'
    }

    response = requests.get(url, headers=headers)

    json_response = json.loads(response.content.decode('utf-8', 'ignore'))
    print(json_response)


    return render(request, 'your_template.html', {'json_data': json_response})

# def import_data_from_url_sport(request):
#     url = 'https://egs.gate.petersburg.ru/egs/sportgrounds/?season=%D0%9B%D0%B5%D1%82%D0%BE&page=1&count=10'
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {JWT_TOKEN}'
#     }
#
#     response = requests.get(url, headers=headers)
#
#     json_response = json.loads(response.content.decode('utf-8', 'ignore'))
#     print(json_response)
#
#
#     return render(request, 'sport_categories.html', {'json_data': json_response})

