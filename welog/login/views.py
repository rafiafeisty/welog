from django.http import HttpResponse
from django.shortcuts import render, redirect
from signup.models import Signup
def login(request):
    return render(request, 'login/index.html')
# Create your views here.
from django.contrib import messages


def checking(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Signup.objects.get(username=email)
            if user.check_password(password):
                request.session['username'] = user.username
                request.session['message'] = True
                return redirect('/allblog/')
        except Signup.DoesNotExist:
            pass

        messages.error(request, 'Invalid username or password')
        return redirect('login:login')

    return redirect('login:login')
