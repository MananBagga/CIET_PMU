from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def home(req):
    return render(req, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after signup
            return redirect('home')  # or wherever you want
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(req):
    return render(req, 'login.html')
