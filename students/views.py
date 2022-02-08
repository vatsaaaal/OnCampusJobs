from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

def student_homepage(request):
    return render(request, 'students/student_homepage.html')

def student_register(request):
    form = CreateUserForm()

    if request.method == "POST":
        user = User()
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.set_password(request.POST.get('password'))
        user.save()

    context = {'form':form}
    return render(request, 'students/student_register.html', context)

def student_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('student_homepage')
        else:
            messages.info(request, 'Username or Password is Incorrect.')


    context = {}
    return render(request, 'students/student_login.html', context)
