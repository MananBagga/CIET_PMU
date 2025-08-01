from admin_dashboard.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q

def login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if not username_or_email or not password:
            messages.error(request, 'All fields are required.')
            return render(request, 'login/login.html')

        try:
            user = User.objects.get(Q(username__iexact=username_or_email) | Q(email__iexact=username_or_email))
        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials.')
            return render(request, 'login/login.html')

        if password != user.password:
            messages.error(request, 'Invalid credentials.')
            return render(request, 'login/login.html')

        request.session['user_id'] = user.id
        request.session['username'] = user.username
        request.session['is_authenticated'] = True

        return redirect('user_dashboard')

    return render(request, 'login/login.html')

def logout_view(request):
    request.session.flush()
    return redirect('home')

