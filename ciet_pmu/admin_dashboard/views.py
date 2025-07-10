from django.shortcuts import render
import json

# Create your views here.
def admin_dashboard(request):
    labels = ['Q1', 'Q2', 'Q3', 'Q4']
    data = [25, 40, 30, 60]

    context = {
        'labels': json.dumps(labels),
        'data': json.dumps(data)
    }
    return render(request, 'admin_dashboard/admin_dashboard.html', context)

def budget(request):
    return render(request, 'admin_dashboard/budget.html')

def projects(request):
    return render(request, 'admin_dashboard/projects.html')