from django.urls import path
from .views import all_books
urlpatterns = [
    path("all_books",all_books,name='books')

]
