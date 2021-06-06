from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Car(models.Model):
    vin = models.CharField(max_length=65, verbose_name='VIN', db_index=True, unique=True)
    color = models.CharField(max_length=25, verbose_name='Цвет')
    brand = models.CharField(max_length=35, verbose_name='Бренд')
    CAR_TYPES = (
        (1, 'Седан'),
        (2, 'Хутчбек'),
        (3, 'Универсал'),
        (4, 'Купе'),
        (5, 'Джип'),
    )
    car_type = models.IntegerField(verbose_name='Тип машины', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)