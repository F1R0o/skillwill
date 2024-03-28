from django import forms
from .models import Car

class UserAddCar(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["model","dzravi","weli"]