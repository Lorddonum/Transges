from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, TicketForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmation') 
    else:
        form = TicketForm()
    return render(request, 'ticket.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def confirmation(request):
    return render(request, 'confirmation.html')
