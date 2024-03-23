from django.shortcuts import render,HttpResponse
from .models import Users
# Create your views here.
def index(requset):
    user = Users()
    return HttpResponse('user zma')


def things(requset):
    user = Users()
    return HttpResponse(user.name,user.last_name)