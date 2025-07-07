from django.shortcuts import render

# Create your views here.
def user_admin(request):
    """
    Render the user administration page.
    """
    return render(request, 'user_admin/user_admin.html')