from django.urls import path

from . import views

app_name = 'pizzas'

urlpatters = [
    path('',views.index, name='index'),
]