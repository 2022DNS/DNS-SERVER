from .models import Road
from detection.drowsy_driving_detection import check_drowsy_driving_based_on_eye_condition
import decimal


def flo2str(coord_val):

    coord_val = round(decimal.Decimal(coord_val), 3)
    coord_val = str(coord_val).split(".")
    return coord_val[0] + '-' + coord_val[1]


def converter(coord_val):
    coord_val = float(coord_val.replace('-','.'))
    coord_val = round(decimal.Decimal(coord_val),3)
    coord_val = str(coord_val).split('.')
    return coord_val[0] + '-' + coord_val[1]


def run(images, la, lo):

    resp = check_drowsy_driving_based_on_eye_condition(images)

    if resp != 1:
        return resp

    data = Road.objects.filter(longitude=lo, latitude=la).get()
    if data:
        data.count = data.count+1
        data.save()
    else:
        Road.objects.create(
            latitude=la,
            longitude=lo
        )
    return resp








