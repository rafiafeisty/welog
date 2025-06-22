from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Signup
from django.contrib.auth.hashers import make_password

def signup(request):
    return render(request, 'signup/index.html')
# Create your views here.


def saving(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create user with properly hashed password
        user = Signup(username=email)
        user.set_password(password)  # Uses make_password internally
        user.save()

        return redirect('login:login')
    return redirect('signup:signup')