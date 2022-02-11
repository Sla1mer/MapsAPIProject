import sys
from io import BytesIO

import requests
from PIL import ImageQt, Image

from Controllers.get_coord_by_name import get_coord
from Controllers.get_map_img import get_map_image
from Models.Variables import coord, spn


def show_map():
    response = get_map_image('l=map', f'll={coord[0]},{coord[1]}', f'spn={spn},{spn}')

    return ImageQt.ImageQt(Image.open(BytesIO(response)))