from .models import Road
from detection.drowsy_driving_detection import check_drowsy_driving_based_on_eye_condition

def changer(flo):

    ##배성준 십년아 여기에 반올림하는 코드짜놔
    flo = str(flo).split(".")
    return flo[0] + '-' + flo[1]

def run(request):

    res_code = check_drowsy_driving_based_on_eye_condition(request.get('images'))
    if res_code != 1:
        return res_code

    la = changer(request.get('latitude'))
    lo = changer(request.get('longitude'))

    data = Road.objects.filter(longitude=lo, latitude=la)#.get()
    if data.exists():
        data.count = data.count+1
        data.save()
    else:
        Road.objects.create(
            latitude=la,
            longitude=lo
        )
    return res_code






