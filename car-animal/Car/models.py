from django.db import models

# Create your models here.
class Car(models.Model):
    model   = models.CharField(max_length=100)
    dzravi = models.CharField(max_length=100)
    weli = models.IntegerField()
    dastukebulia  = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.model}"
    
    