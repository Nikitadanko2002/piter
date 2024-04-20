import json

from django.shortcuts import HttpResponse

from PiterskiyDvish.settings import JWT_TOKEN
from .models import Beautiful
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

