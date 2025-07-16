from django.shortcuts import render, redirect
import json
import datetime
from .models import User, Program, Annualbudget

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
    if request.method == 'POST':
        program_budget = request.POST.get('program_budget')
        budget_date = request.POST.get('budget_date') 
        parsed_date = datetime.datetime.strptime(budget_date, '%Y-%m-%d')
        year = parsed_date.year

        Annualbudget.objects.create(budget=program_budget, year=year)
    return render(request, 'admin_dashboard/budget.html')

# def projects(request):
#     users = User.objects.all()

#     if request.method == 'POST':
#         program_type = request.POST.get('program_type')
#         program_title = request.POST.get('program_title')
#         program_coordinator = request.POST.get('program_coordinator')  # This will be a string
#         program_coordinator_id = User.objects.get(id=program_coordinator)


#         # Fetch the latest AnnualBudget instance (or you can filter by year or something else)
#         try:
#             annual_budget = Annualbudget.objects.latest('year')  # Adjust logic if needed
#         except Annualbudget.DoesNotExist:
#             annual_budget = None

#         if program_type and program_title and annual_budget:
#             program = Program.objects.create(
#                 type=program_type,
#                 title=program_title,
#                 coordinator_id=program_coordinator_id,
#                 annual_budget=annual_budget
#             )
#             return redirect('projects')  # Or wherever you want to redirect

#     return render(request, 'admin_dashboard/projects.html', {'users': users})

from django.shortcuts import render, redirect
from .models import User, Program, Annualbudget

def projects(request):
    users = User.objects.all()

    if request.method == 'POST':
        program_type = request.POST.get('program_type')
        program_title = request.POST.get('program_title')
        coordinator = request.POST.get("program_coordinator")
        program_budget = request.POST.get('program_budget')
        program_sub_type = request.POST.get('program_sub_type')
        try:
            # coordinator_id = User.objects.get(username=coordinator).id
            latest_budget = Annualbudget.objects.latest('year')  

            Program.objects.create(
                type=program_type,
                title=program_title,
                coordinator_id=coordinator,
                annual_budget_id=latest_budget.id,
                program_budget=program_budget,
                program_sub_type=program_sub_type
            )

            return redirect('projects')  # clear POST

        except (User.DoesNotExist, Annualbudget.DoesNotExist) as e:
            print("Error:", e)

    return render(request, 'admin_dashboard/projects.html', {'users': users})
