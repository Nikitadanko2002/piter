# import requests
#
# from PiterskiyDvish.settings import JWT_TOKEN
#
# url = 'https://spb-afisha.gate.petersburg.ru/kg/external/afisha/categories'
# headers = {
# 'Content-Type': 'application/json',
# 'Authorization': f'Bearer {JWT_TOKEN}'
# }
#
# response = requests.get(url, headers=headers)
#
#
# json_response = response.json()
# print(json_response)
# count = json_response['count']
# results = json_response['results']
#
# for item in results:
#     my_model = Beautiful(
#     oid=item['oid'],
#     name=item['name'],
#     name_en=item['name_en'],
#     address_manual=item['address_manual'],
#     phone=item['phone'],
#     www=item['www'],
#     email=item['email'],
#     kitchen=item.get('kitchen'),
#     for_disabled=item['for_disabled'],
#     coord=item['coord']
#     )
#     my_model.save()