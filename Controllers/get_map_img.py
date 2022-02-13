import requests


def get_map_image(*all_params):
    base_request = f"http://static-maps.yandex.ru/1.x/?"
    for i in all_params:
        base_request += f"&{i}"
    print(base_request)
    image = requests.get(base_request).content
    return image

# тестовый запрос
# get_map_image('l=map', 'pt=37.560161,55.791477~37.644923,55.701981')
