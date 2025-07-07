from django.shortcuts import render, redirect
from user_admin.models import User  # Make sure your User model is defined properly
from django.contrib import messages  # Optional for feedback messages

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Basic validation (optional, you can improve this)
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            User.objects.create(username=username, name=name, email=email, password=password, role='Coordinator')
            messages.success(request, 'Account created successfully.')
            return redirect('login')  # Replace 'login' with your login URL name

    return render(request, 'signup/signup.html')
