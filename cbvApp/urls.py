from django.urls import include, path
from .views import StudentListView, StudentDetailView

urlpatterns = [
    path('student/', StudentListView.as_view(), name='student-list'),
    path('student/<int:pk>', StudentDetailView.as_view(), name='student-detail')
]