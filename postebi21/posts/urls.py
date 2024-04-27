from django.urls import path
from .views import UserCreateAPIView,UserLoginAPIView,UserLogoutAPIView,AllPostAPI,PostCreateAPI,PostDetail

urlpatterns = [
    path("register/",UserCreateAPIView.as_view(),name="register"),
    path("login/",UserLoginAPIView.as_view(),name="login"),
    path("logout/",UserLogoutAPIView.as_view,name="logout"),
    path("",AllPostAPI.as_view(),name="allposts"),
    path("create-post/",PostCreateAPI.as_view(),name="create-post"),
    path("post-detial/<int:pk>/",PostDetail.as_view(),name="post-detail"),
]
