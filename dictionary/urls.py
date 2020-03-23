from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meaning', views.meaning, name='meaning'),
]
