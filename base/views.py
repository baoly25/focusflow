from .forms import SignUpForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from .forms import EmailAuthenticationForm
from django.shortcuts import render
from .models import Journal
from .forms import JournalForm
from django.contrib.auth.decorators import login_required


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

def pomodoro_timer(request):
    return render(request, 'pomodoro.html')

@login_required
def journal_list(request):
    journals = Journal.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'journal/list.html', {'journals': journals})

@login_required
def journal_create(request):
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            journal = form.save(commit=False)
            journal.user = request.user
            journal.save()
            return redirect('journal_list')
    else:
        form = JournalForm()
    return render(request, 'journal/create.html', {'form': form})

@login_required
def journal_edit(request, pk):
    journal = get_object_or_404(Journal, pk=pk, user=request.user)
    if request.method == 'POST':
        form = JournalForm(request.POST, instance=journal)
        if form.is_valid():
            form.save()
            return redirect('journal_list')
    else:
        form = JournalForm(instance=journal)
    return render(request, 'journal/edit.html', {'form': form, 'journal': journal})
