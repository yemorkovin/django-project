from django.db import models
from django.forms import CharField


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=200, verbose_name="status")
    full_name = models.CharField(max_length=200, verbose_name="full_name")
    tel = models.CharField(max_length=200, verbose_name="tel")
    email = models.CharField(max_length=200, verbose_name="email")
    login = models.CharField(max_length=200, verbose_name="login")
    password = models.CharField(max_length=200, verbose_name="password")
    city = models.CharField(max_length=200, verbose_name="city", default='')
    # photo = models.CharField(max_length=200,  verbose_name="photo", default=None)

    def __str__(self):
        return self.full_name
    


class Photo_list(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="full_name")
    photo = models.CharField(max_length=200, verbose_name="image")
    login = models.CharField(max_length=200, verbose_name="login")
    
class City_list(models.Model):
    login = models.CharField(max_length=200, verbose_name="login")
    city = models.CharField(max_length=200, verbose_name="city")
   
    def __str__(self) -> str:
        return self.city

class Photo_Profile(models.Model):
    photo_profile = models.CharField(max_length=400, verbose_name="photo_profile")
    login = models.CharField(max_length=200, verbose_name="login")

    
