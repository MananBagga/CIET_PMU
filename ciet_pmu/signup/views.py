from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from admin_dashboard.models import User
import re

def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

def is_strong_password(password):
    return (
        len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'\d', password) and
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    )

def is_valid_username(username):
    return re.match(r'^[a-zA-Z0-9_]{3,30}$', username) is not None

def is_valid_name(name):
    return re.match(r'^[A-Za-z ]+$', name) is not None

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        context = {'username': username, 'name': name, 'email': email}

        # ---- Basic Validations ----
        if not all([username, name, email, password, confirm_password]):
            messages.error(request, 'All fields are required.')
            return render(request, 'signup/signup.html', context)

        if not is_valid_username(username):
            messages.error(request, 'Username must be 3–30 characters and only contain letters, numbers, and underscores.')
            return render(request, 'signup/signup.html', context)

        if not is_valid_name(name):
            messages.error(request, 'Name can only contain alphabets and spaces.')
            return render(request, 'signup/signup.html', context)

        if not is_valid_email(email):
            messages.error(request, 'Invalid email format.')
            return render(request, 'signup/signup.html', context)

        if not is_strong_password(password):
            messages.error(request, 'Password must be at least 8 characters long, include uppercase, lowercase, digit, and special character.')
            return render(request, 'signup/signup.html', context)

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup/signup.html', context)

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'signup/signup.html', context)

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'signup/signup.html', context)

        user = User(username=username, name=name, email=email, role='Coordinator', password=password)
        user.save()

        messages.success(request, 'Account created successfully.')
        return redirect('login')

    return render(request, 'signup/signup.html')
