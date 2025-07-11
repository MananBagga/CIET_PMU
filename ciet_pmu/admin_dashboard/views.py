from django.shortcuts import render, redirect
import json
from .models import User, Program

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
    users = User.objects.all()

    if request.method == 'POST':
        program_type = request.POST.get('program_type')
        program_title = request.POST.get('program_title')
        program_coordinator_id = request.POST.get('program_coordinator')

        try:
            coordinator = User.objects.get(id=program_coordinator_id)

            Program.objects.create(
                type=program_type,
                title=program_title,
                coordinator=coordinator,  # ForeignKey to User
            )
            return redirect('projects')
        
        except User.DoesNotExist:
            # Handle the case where the coordinator does not exist
            return render(request, 'admin_dashboard/projects.html', {
                'users': users,
                'error': 'Selected coordinator does not exist.'
            })
        
        except Exception as e:
            # Handle any other exceptions
            return render(request, 'admin_dashboard/projects.html', {
                'users': users,
                'error': f'An error occurred: {str(e)}'
            })
        
    return render(request, 'admin_dashboard/projects.html', {'users': users})


   

