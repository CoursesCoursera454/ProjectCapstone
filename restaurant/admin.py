from django.contrib import admin
from . import models


#Create models

admin.site.register(models.Booking)
admin.site.register(models.Menu)