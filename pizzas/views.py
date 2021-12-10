from django.shortcuts import render, redirect
from .models import Pizza
from .forms import CommentsForm

# Create your views here.

def index(request):
    '''Home page for pizzeria'''
    return render(request, 'pizzas/index.html')



def pizzas(request):                 #whatever you named the view in URLs must be received in views with
                                     #the exact same function name
    pizzas = Pizza.objects.order_by('name')
   
    context = {'pizzas':pizzas}                #use context to populate the HTML template with data (pass data to html)
                                               #context is a dictionary- key is variable used in template file, value is variable used in views function

    return render(request, 'pizzas/pizzas.html',context)



def pizza(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)     #urls.py calls a variable called pizza_id which is defined here, SO MUST BE THE SAME
     #calls the Pizza model (class/object)
    toppings = pizza.topping_set.all()         #foregin key accessed using '_set'
    comments = pizza.comment_set.all()         #all() iterates through the database and retreives
    context = {'pizza':pizza, 'toppings':toppings, 'comments':comments}

    return render(request, 'pizzas/pizza.html',context)
                                                        # "." notation pulls the attributes in OOP


def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)    #first, determines which pizza the comment will be written under

    if request.method != 'POST':              #if the request is GET- requesting a form from the webserver
        form = CommentsForm()                 #loads an empty form
    else:
        form = CommentsForm(data=request.POST)  #if the request if POST- take data from the webpage (form) and save it in the (database)
                                                #POST = FILLING OUT THE FORM- WRITING TO DATABASE
        if form.is_valid():
            new_comment = form.save(commit=False)   #tells database we're not ready to write to the form yet
            new_comment.pizza = pizza               #assigns the comment to a pizza
            new_comment.save()
            return redirect('pizzas:pizza',pizza_id=pizza_id)  

    context = {'form': form, 'pizza': pizza}
    return render(request, 'pizzas/new_comment.html',context)
