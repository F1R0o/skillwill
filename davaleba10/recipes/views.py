from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Recipes
from .serializers import RecipeSerializer





class Paginator(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100


class RetrieveRecipe(ListAPIView):
    queryset  = Recipes.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = Paginator
    permission_classes = [AllowAny]
    





class SearchRecipeAPIView(ListAPIView):
    queryset  = Recipes.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    pagination_class = Paginator
    permission_classes = [AllowAny]


    

   

class FilterRecipesByAuthor(ListAPIView):
    queryset  = Recipes.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = Paginator
    permission_classes = [AllowAny]
    filterset_fields = ['author__name'] 
   

   




class RetriveRecipeById(RetrieveUpdateDestroyAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [AllowAny]

