from .models import Road
from detection.drowsy_driving_detection import check_drowsy_driving_based_on_eye_condition

class CoordinateChanger:

    def changer(self, longitude: Road, latitude: Road):
        Road.save()

