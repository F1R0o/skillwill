from .models import Recipes
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = '__all__'
        ordering = ['-id']