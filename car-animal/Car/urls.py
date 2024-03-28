
from django.urls import path
from .views import SelectCar,AddCar,DeleteCar,UpdateCar,SearchCar,useradd,all_cars,car_by_id
urlpatterns = [
    path("",SelectCar.as_view(),name="main_car"),
    path("<int:id>",SelectCar.as_view(),name="maind_car"),
    path("add",AddCar.as_view(),name="add_car"),
    path("delete/<int:id>/",DeleteCar.as_view(),name="delete_car"),
    path("update/<int:pk>/",UpdateCar.as_view(),name="UpdateCAR"),
    path('search/',SearchCar.as_view(),name="search"),
    path("user_add",useradd,name="user_add"),
    path("all_cars/",all_cars,name="all_cars"),
    path("user/<int:id>",car_by_id,name="car_by_id")
]
