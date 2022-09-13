from .models import Road
import decimal
from detection.drowsy_driving_detection import check_drowsy_driving_based_on_eye_condition


def flo2str(flo):
    flo = str(flo).split(".")
    return flo[0] + '-' + flo[1]

class CoordinateChanger:

    def changer(self, longitude: Road, latitude: Road):
        Road.save()



