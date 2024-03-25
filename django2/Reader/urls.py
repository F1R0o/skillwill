
from django.urls import path
from .views import user_auth
urlpatterns = [
    path("",user_auth,name="auth")
  
]
