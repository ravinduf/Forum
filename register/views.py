from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            print(username)
            user = authenticate(request,username=username, password=password)
            login(request, user)
            return redirect('/')

    else:
        form = RegisterForm()

    return render(request, "register/register.html", {'form':form})
