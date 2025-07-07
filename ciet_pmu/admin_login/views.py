from django.shortcuts import render

# Create your views here.
def admin_login(request):
    """
    Render the admin login page.
    """
    return render(request, 'admin_login/admin_login.html')