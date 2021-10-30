from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate

# Create your views here.


def signupuser(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'GET':
            return render(request, 'registration/signup.html', {'form': UserCreationForm()})
        else:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'], first_name=request.POST['firstname'])
            user.save()
            login(request, user)
            return redirect('homepage')

def loginuser(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            user = authenticate(request,username = request.POST['username'], password = request.POST['password'])
            if user is None: 
                return render(request, 'registration/login.html', {'form': AuthenticationForm() ,'error': 'Username or Password is incorrect'})
            else:
                login(request, user)
                return redirect('homepage')
        else:
            return render(request, 'registration/login.html', {'form': AuthenticationForm()})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect ('homepage')