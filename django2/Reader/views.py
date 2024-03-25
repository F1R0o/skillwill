from django.shortcuts import render,HttpResponse,redirect
from .form import user_form

# Create your views here.
def user_auth(request):
    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            return redirect('books')
    else:
        form = user_form()
    return render(request, 'login.html', {'form': form})