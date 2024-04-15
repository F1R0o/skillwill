from django.db import models
from author.models import Author
# Create your models here.

class Recipes(models.Model):
    title  = models.CharField(max_length=100)
    description  = models.TextField()
    created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


    def __str__(self):
        return f"{self.title}"