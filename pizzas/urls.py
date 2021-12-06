from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    path('',views.index, name='index'),
    path('pizzas',views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/',views.pizza,name='pizza')
]