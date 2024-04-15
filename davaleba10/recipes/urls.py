from django.urls import path
from .views import RetrieveRecipe,RetriveRecipeById,SearchRecipeAPIView,FilterRecipesByAuthor
urlpatterns = [
    path("",RetrieveRecipe.as_view(),name="RERTIVEAPI"),
    path("recipe/<int:pk>/",RetriveRecipeById.as_view(),name="RETRIVEBYID"),
    path("search/",SearchRecipeAPIView.as_view(),name='SEARCHAPI'),
    path('filter-by-author/', FilterRecipesByAuthor.as_view(), name='filter_by_author'),

]
