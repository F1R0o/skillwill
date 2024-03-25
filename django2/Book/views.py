from django.shortcuts import render

# Create your views here.
def all_books(request):
    books = {"books":[ {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "1984", "author": "George Orwell"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"title": "Pride and Prejudice", "author": "Jane Austen"},
    {"title": "Moby-Dick", "author": "Herman Melville"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien"},
    {"title": "War and Peace", "author": "Leo Tolstoy"},
    {"title": "Brave New World", "author": "Aldous Huxley"},
    {"title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez"}]}   
    return render(request,"books.html", books)

# Print the list of books
