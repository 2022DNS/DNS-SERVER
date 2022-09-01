from django.db import models
from django.conf import settings

class Road_info(models.Model):
    id = models.IntegerField() # 위도 경도 다르더라도 같은 id로 묶으면 될듯?
    longitude = models.IntegerField() # 경도
    latitude = models.IntegerField() # 위도
    count = models.IntegerField() # 졸음횟수

class image:
    id = models.IntegerField()
    image_id = models.IntegerField()
