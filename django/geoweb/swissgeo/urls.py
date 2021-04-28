from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('city/', views.cities, name='cities'),
    path('city/<int:city_id>', views.city, name='city'), 
    path('cantons', views.cantons, name='cantons'),
    path('cantons/<str:canton_name>', views.canton, name='canton'),
    path('cantons.json', views.cantonsjson, name='cantonsjson'),
]
