from admin_dashboard.models import User, Pmuadmin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if not username or not password:
            messages.error(request, 'All fields are required.')
            return render(request, 'login/login.html')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials.')
            return render(request, 'login/login.html')

        if password == user.password:
            # Manually set session variables
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['is_authenticated'] = True
            return redirect('user_dashboard', user_id=user.id)
            # return redirect('user_dashboard')
        else:
            messages.error(request, 'Invalid credentials.')

    return render(request, 'login/login.html')


# def login(request):
#     if request.method == 'POST':
#         uusername= request.POST["username"]
#         ppasssword = request.POST['password']
#         selection_list = User.objects.filter(username= uusername, password =ppasssword).all()
#         for p in selection_list:
#             print(p.username)
#             print(p.password)
#             user = auth.authenticate(uusername=p.username, ppasssword=p.password)
#             request.session['user_id'] = p.id
#             request.session['username'] = p.username
#             return redirect('/user_dashboard')
#         else:
#             messages.success(request,'Wrong username and Password')
#     return render(request,'login/login.html')


def logout_view(request):
    request.session.flush()
    return redirect('home')
