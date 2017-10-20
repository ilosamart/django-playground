from django.conf.urls import url
from .views import CityList, StateList, CountryList

app_name = 'locations'

urlpatterns = [
    url(r'^city/', CityList.as_view()),
    url(r'^state/', StateList.as_view()),
    url(r'^country/', CountryList.as_view()),
]
