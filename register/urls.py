from django.urls import path
from . import views

urlpatterns = [
    #  Для тесту http://127.0.0.1:8000/app1_forms/register/
    path('', views.register, name='register'),
]
