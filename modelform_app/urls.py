from django.urls import path
from . import views

urlpatterns = [
    #  Для тесту http://127.0.0.1:8000/modelform_app/
    path('', views.create_article, name='create_article'),
]
