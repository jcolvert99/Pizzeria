from django.contrib import admin

# Register your models here.
from .models import Pizza, Topping, Comment   # "." in front tells django to look for models.py in same directory as admin.py

admin.site.register(Pizza)    #tells Django to manage our model through the admin site
admin.site.register(Topping)
admin.site.register(Comment)
