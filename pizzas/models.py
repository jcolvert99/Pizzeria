from django.db import models


# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=200)         #models define the data we want to manage in our app in the form of a class

    def __str__(self):
        return self.name



class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)  #each topping is only assigned to one pizza
    name = models.TextField()

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        return self.name



class Comment(models.Model):       #has fields called pizza, text, and date_added
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'comments'
    
    def __str__(self):
        return self.text