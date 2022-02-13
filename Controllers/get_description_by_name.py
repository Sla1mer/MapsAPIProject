import requests


def get_description(name):
    API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'
    request_to_get_coord = f"http://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={name}&format=json"
    coord_respone = requests.get(request_to_get_coord)
    json_coord_respone = coord_respone.json()
    answ = json_coord_respone["response"]["GeoObjectCollection"]["featureMember"] \
        [0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
    all_info = ''
    for info in answ:
        all_info += f"{info['name']}\n"
    return all_info



# python3 get_description_by_name.py