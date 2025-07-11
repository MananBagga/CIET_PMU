from django.shortcuts import render, redirect
from admin_dashboard.models import User
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login(request):
    
    if request.method == 'GET':
        username = request.GET.get('username', '').strip()
        password = request.GET.get('password', '')

        if not username or not password:
                messages.error(request, 'All fields are required.')
                return render(request, 'login/login.html')
        
        if User.objects.filter(username=username, password=password).exists():
            request.session['username'] = username
            
            return redirect('user_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            # user = User.objects.get(username=username, password=password)
            # if user.role == 'Coordinator':
            # else:
            #     messages.error(request, 'You do not have permission to access this page.')
            #     return render(request, 'login/login.html')

    return render(request, 'login/login.html')

def logout_view(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('home')