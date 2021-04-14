from django.shortcuts import render
from django.http import HttpResponse
from .models import City
from django.template import loader
from django.http import Http404


# Create your views here.
def index(request):    
   return HttpResponse("Hi there this is Switzerland")

def cities(request):
    top_cities=City.objects.order_by('-city_name')[:5]
    #template = loader.get_template('swissgeo/cities.html')
    context={'top_cities':top_cities}
    #output = ','.join([c.city_name for c in top_cities])
    #return HttpResponse(template.render(context,request))
    return render(request,'swissgeo/cities.html',context)


def city(request,city_id):
    try:
        city=City.objects.get(pk=city_id)
    except City.DoesNotExist:
        raise Http404("city not found!!")
    
    return render(request,'swissgeo/city.html',{'city':city})