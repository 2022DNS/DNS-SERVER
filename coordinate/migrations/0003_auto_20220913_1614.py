# Generated by Django 3.2.9 on 2022-09-13 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinate', '0002_alter_road_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='road',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='졸음 발생 시간'),
        ),
        migrations.AlterField(
            model_name='road',
            name='latitude',
            field=models.CharField(max_length=20, verbose_name='위도'),
        ),
        migrations.AlterField(
            model_name='road',
            name='longitude',
            field=models.CharField(max_length=20, verbose_name='경도'),
        ),
    ]
