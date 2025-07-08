from django.shortcuts import render

# Create your views here.
def admin_dashboard(request):
    """
    Render the admin dashboard page.
    """
    return render(request, 'admin_dashboard/admin_dashboard.html')

def budget(request):
    """
    Render the set annual budget page.
    """
    return render(request, 'admin_dashboard/budget.html')

def projects(request):
    """
    Render the projects page.
    """
    return render(request, 'admin_dashboard/projects.html')