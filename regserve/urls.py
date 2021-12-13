from django.urls import path
from . import views

##Page for paths

urlpatterns = [
    path('', views.index, name="index"),
    path('data/students/', views.StudentListView.as_view(), name='api_students'),
    path('/students/', views.StudentListForm.as_view(), name='students'),
    path('/createstudents/', views.StudentCreateForm.as_view(), name='create_students'),
]