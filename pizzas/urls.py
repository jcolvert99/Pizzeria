from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    path('',views.index, name='index'),
    path('pizzas',views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/',views.pizza,name='pizza'),   #individual pizza page
                                                               #<int:pizza_id>: creates an integer variable that references the primary key of pizzas table
    path('new_comment/<int:pizza_id>/',views.new_comment, name='new_comment'),
]