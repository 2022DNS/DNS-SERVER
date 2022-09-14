from .models import Road
from detection.drowsy_driving_detection import check_drowsy_driving_based_on_eye_condition

def flo2str(flo):
    flo = str(flo).split(".")
    return flo[0] + '-' + flo[1]

def run(request):
    res_code = check_drowsy_driving_based_on_eye_condition(request.get('images'))
    if res_code == 1:
        la = request.get('latitude')
        lo = request.get('longitude')
        Road.objects.create(
            latitude=la,
            longitude=lo
        )
    else:
        return res_code






