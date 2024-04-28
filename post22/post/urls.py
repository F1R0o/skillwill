from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView,AllPostAPI,CreatePostAPI,logoutAPI,UpdateAPI


urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path("logout/",logoutAPI,name='logout'),
    path("",AllPostAPI.as_view(),name='all-post'),
    path("create-post/",CreatePostAPI.as_view(),name="create-post"),
    path("update/<int:pk>",UpdateAPI.as_view(),name='update')
]