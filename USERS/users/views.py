from django.shortcuts import render,redirect,get_object_or_404
from .models import Users
from .forms import CreateUser
# Create your views here.
def all_users(request):
    if request.path == '/update/':
        users = Users.objects.all()
        context = {'user':users}
        return render(request,"users/all_update.html",context)
    elif request.path == "/delete/":
        users = Users.objects.all()
        context = {'user':users}
        return render(request,"users/all_delete.html",context)

    else:
        users = Users.objects.all()
        context = {'user':users}
        return render(request,"users/all.html",context)




def create_user(request):
    if request.method == "POST":
        form = CreateUser(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("ALLUSERS")
    else:
        form = CreateUser()

    return render(request,"users/create.html",context={"form":form})


def user_by_id(request,id):
    user = Users.objects.get(pk=id)
    redirect_to  = {"user":user}
    return render(request,"users/userid.html",redirect_to)








def update_user(request, id):
    user = get_object_or_404(Users, pk=id)
    if request.method == 'POST':
        form = CreateUser(request.POST, request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('ALLUSERS')
    else:
        form = CreateUser(instance=user)
    
    return render(request, 'users/update.html', {'form': form})




def delete_by_id(request, id):
    user = get_object_or_404(Users, pk=id)
    if request.method == 'POST':
        user.delete()
        return redirect('ALLUSERS')
    return render(request, 'users/delete.html', {'user': user})