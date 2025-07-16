from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from admin_dashboard.models import User
from django.contrib.auth.hashers import make_password


# User = get_user_model()

def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        context = {'username': username, 'name': name, 'email': email}

        if not all([username, name, email, password, confirm_password]):
            messages.error(request, 'All fields are required.')
            return render(request, 'signup/signup.html', context)

        if not is_valid_email(email):
            messages.error(request, 'Invalid email format.')
            return render(request, 'signup/signup.html', context)

        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
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

        # hashed_password = make_password(password)
        user = User(username=username, name=name, email=email, role='Coordinator', password=password)
        user.save()

        messages.success(request, 'Account created successfully.')
        return redirect('login')

    return render(request, 'signup/signup.html')
