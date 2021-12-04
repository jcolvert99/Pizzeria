import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza, Topping

topics = Pizza.objects.all() #same as saying select * from in SQL- pulls all rows

for topic in topics:
    print(topic.id)         #called NoSQL
    print(topic.name)       # "." notation pulls the attributes in OOP
       #if you just pring topic then it will say "Topic Object 2" because hasn't processed the str function

t = Pizza.objects.get(id=1)
print(t)
