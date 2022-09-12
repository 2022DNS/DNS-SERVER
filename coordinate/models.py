from django.db import models
from django.conf import settings

class Road(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    longitude = models.FloatField(
        null=False,
        blank=False,
        verbose_name="경도"
    )
    latitude = models.FloatField(
        null=False,
        blank=False,
        verbose_name="위도"
    )
    count = models.IntegerField(
        default=1,
        verbose_name="졸음 횟수"

    ) # 졸음횟수
    date = models.DateTimeField(
        null=False,
        blank=False,
        auto_now=True,
        verbose_name="졸음 발생 시간"
    )