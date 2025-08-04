from django.shortcuts import render, redirect
from django.contrib import messages
from admin_dashboard.models import Pmuadmin

# Create your views here.
def admin_login(request):

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if not username or not password:
                messages.error(request, 'All fields are required.')
                return render(request, 'admin_login/admin_login.html')
        
        try:
            admin = Pmuadmin.objects.get(username=username)
        except Pmuadmin.DoesNotExist:
            messages.error(request, 'Invalid credentials.')
            return render(request, 'admin_login/admin_login.html')

        if password == admin.password:
            request.session['user_id'] = admin.id
            request.session['username'] = admin.username
            request.session['is_authenticated'] = True
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid credentials.')

    return render(request, 'admin_login/admin_login.html')