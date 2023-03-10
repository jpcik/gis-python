from django.contrib import admin
from django.contrib.gis import admin

from .models import City, Hospital, Canton

# Register your models here.
admin.site.register(City)
admin.site.register(Hospital) 
admin.site.register(Canton, admin.OSMGeoAdmin)

