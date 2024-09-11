from django.db import models

# Create your models here.


class Machine(models.Model): 
    name = models.CharField(max_length=40)
    has_coin_acceptor = models.BooleanField()


    def __str__(self):
        return self.name