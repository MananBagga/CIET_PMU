from django.shortcuts import render, redirect
import json
import datetime
from .models import User, Program, Annualbudget

# Create your views here.
def admin_dashboard(request):
    budget = Annualbudget.objects.all()
    return render(request, 'admin_dashboard/admin_dashboard.html', {'budget':budget})

def budget(request):
    if request.method == 'POST':
        program_budget = request.POST.get('program_budget')
        budget_date = request.POST.get('budget_date') 
        parsed_date = datetime.datetime.strptime(budget_date, '%Y-%m-%d')
        year = parsed_date.year

        Annualbudget.objects.create(budget=program_budget, year=year)
    return render(request, 'admin_dashboard/budget.html')

def projects(request):
    users = User.objects.all()

    if request.method == 'POST':
        program_type = request.POST.get('program_type')
        program_title = request.POST.get('program_title')
        coordinator = request.POST.get("program_coordinator")
        program_budget = request.POST.get('program_budget')
        program_sub_type = request.POST.get('program_sub_type')
        try:
            latest_budget = Annualbudget.objects.latest('year')  

            Program.objects.create(
                type=program_type,
                title=program_title,
                coordinator_id=coordinator,
                annual_budget_id=latest_budget.id,
                program_budget=program_budget,
                program_sub_type=program_sub_type
            )

            return redirect('projects')

        except (User.DoesNotExist, Annualbudget.DoesNotExist) as e:
            print("Error:", e)

    return render(request, 'admin_dashboard/projects.html', {'users': users})
