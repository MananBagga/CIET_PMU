from django.shortcuts import render, redirect
from django.contrib import messages
from admin_dashboard.models import Pmuadmin
from django.db.models import Q

def admin_login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if not username_or_email or not password:
            messages.error(request, 'All fields are required.')
            return render(request, 'admin_login/admin_login.html')

        try:
            admin = Pmuadmin.objects.get(Q(username__iexact=username_or_email) | Q(email__iexact=username_or_email))
        except Pmuadmin.DoesNotExist:
            messages.error(request, 'Invalid credentials.')
            return render(request, 'admin_login/admin_login.html')

        if password != admin.password:
            messages.error(request, 'Invalid credentials.')
            return render(request, 'admin_login/admin_login.html')

        request.session['admin_id'] = admin.id
        request.session['admin_username'] = admin.username
        request.session['is_admin_authenticated'] = True

        return redirect('admin_dashboard')

    return render(request, 'admin_login/admin_login.html')
