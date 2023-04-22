from django.contrib import admin

from yourphoto.models import City_list, Photo_list, Photo_Profile, Users

admin.site.register(Users)
admin.site.register(Photo_list)
admin.site.register(City_list)
admin.site.register(Photo_Profile)


# Register your models here.
