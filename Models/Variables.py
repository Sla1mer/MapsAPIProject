from Controllers.get_coord_by_name import get_coord

coord = get_coord("ул. Гайдара, 6, Калининград, Россия")
spn = 0.003


def change_spoon(value: float):
    global spn
    spn += value