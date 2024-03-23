from django.shortcuts import render,HttpResponse
from .models import Calendar
# Create your views here.
def index(request):
    return HttpResponse("zma")


def calendar(request):
    calendar = Calendar()
    return HttpResponse (calendar)
    