from django.contrib.gis import admin

from .models import City, Hospital, Canton

admin.site.register(City)
admin.site.register(Hospital) 
admin.site.register(Canton, admin.ModelAdmin)
