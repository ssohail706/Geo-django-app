from django.http.response import HttpResponse
from django.views.generic import DetailView
from .models import City
import requests
import json


class CitiesDetailView(DetailView):
    """
        City detail view.
    """
    template_name = 'cities/city-detail.html'
    model = City


def weather(request):
   token =  "23bc6ab8019029a149bb3b47050190a5"
   long = request.POST['lon']
   lat = request.POST['lat']
   lat_long = "lat=" + str(lat)+ "&lon=" + str(long)
   coord_API_endpoint = "http://api.openweathermap.org/data/2.5/weather?"
   lat_long = "lat=" + str(lat)+ "&lon=" + str(long)
   join_key = "&appid=" + str(token)
   units = "&units=metric"
   current_coord_weather_url= coord_API_endpoint + lat_long + join_key + units
   json_data = requests.get(current_coord_weather_url).json()
   temp = json_data['main']['temp']
   humidity = json_data['main']['humidity']
   response = {'temp':temp,'humidity':humidity}
   #Send the response 
   return HttpResponse(json.dumps( response ))

