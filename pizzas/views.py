from django.shortcuts import render

from pizzas.models import Pizza

# Create your views here.

def index(request):
    '''Home page for pizzeria'''
    return render(request, 'pizzas/index.html')


def pizzas(request):
    pizzas = Pizza.objects.order_by('name')

    context = {'pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html',context)