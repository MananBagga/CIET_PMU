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
                return render(request, 'login/login.html')
        
        if Pmuadmin.objects.filter(username=username, password=password).exists():
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            # user = User.objects.get(username=username, password=password)
            # if user.role == 'Coordinator':
            # else:
            #     messages.error(request, 'You do not have permission to access this page.')
            #     return render(request, 'login/login.html')

    return render(request, 'admin_login/admin_login.html')