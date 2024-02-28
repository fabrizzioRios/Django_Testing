
from django.urls import include, path
from .views import create_list_passenger, detail_passenger

urlpatterns = [
    path('passenger/', create_list_passenger,
         name='passenger'),
    path('passenger/<int:pk>', detail_passenger,
         name='passenger_detail'),
]
