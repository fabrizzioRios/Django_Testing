
from django.urls import include, path
from .views import student_list, student_detail

urlpatterns = [
    path('student/', student_list, name='student-list'),
    path('student/<int:pk>', student_detail, name='student-detail')
]