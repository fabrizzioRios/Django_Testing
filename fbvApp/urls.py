
from django.urls import include, path
from .views import student_list

urlpatterns = [
    path('', student_list, name='students')
]