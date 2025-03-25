from .forms import SignUpForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import EmailAuthenticationForm
from django.shortcuts import render


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    form = EmailAuthenticationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        auth_login(request, user)
        return redirect('home')
    return render(request, 'registration/login.html', {'form': form})

def homepage(request):
    return render(request, 'homepage.html')