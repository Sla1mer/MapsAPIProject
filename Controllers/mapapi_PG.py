from io import BytesIO

from PIL import ImageQt, Image

from Controllers.get_map_img import get_map_image
from Models.Variables import coord, spn


def show_map():
    response = get_map_image('l=map', f'll={coord[0]},{coord[1]}', f'spn={spn[0]},{spn[0]}')
    print(spn)

    return ImageQt.ImageQt(Image.open(BytesIO(response)))