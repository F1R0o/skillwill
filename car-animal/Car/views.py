from django.shortcuts import render,HttpResponse,get_object_or_404
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import generics
from .serializers import CarSerializer
from .models import Car
from .forms import UserAddCar
# Create your views here.

class SelectCar(APIView):
    def get(self,request,id=None):
        if id:
            data = Car.objects.get(pk=id)
            serializer = CarSerializer(data,context={"request":request},many=False)
            return Response(serializer.data)
        data = Car.objects.all()
        serializer = CarSerializer(data,context={"request":request},many=True)
        return Response(serializer.data)
    

class AddCar(APIView):
    def post(self,request):
            data = CarSerializer(data=request.data,many=False)
            if data.is_valid():
                data.save()
                return Response(data.data)
            return Response(data.errors)


class DeleteCar(APIView):
    def delete(self,request,id):
        data = Car.objects.get(pk=id)
        data.delete()
        serializer = CarSerializer(data,context={"request":request},many=False)
        return Response(serializer.data)

         



class UpdateCar(APIView):
    def put(self, request, pk):
        obj = Car.objects.get(id=pk)
        serializer = CarSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    


class SearchCar(generics.ListCreateAPIView):
    search_fields = ["model","weli"]
    filter_backends = (filters.SearchFilter,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer




def useradd(request):
    form = UserAddCar()
    if request.method == "POST":
        form = UserAddCar(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("zmaxar")
    return render(request,"Car/add_cars_form.html",context={"form":form})


def all_cars(request):
    cars = Car.objects.all()
    return render(request,"Car/all.html",{"cars":cars})


def car_by_id(request, id):
    car = get_object_or_404(Car, pk=id)
    context = {"car": car}
    return render(request, "Car/detail.html", context)