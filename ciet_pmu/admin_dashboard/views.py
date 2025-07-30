from django.shortcuts import render, redirect, get_object_or_404
import datetime
import calendar
from .models import User, Program, Annualbudget, Pmuadmin, Projectreport
from openpyxl import Workbook
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
import io
from django.contrib import messages


def admin_dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('admin_login')

    admin = get_object_or_404(Pmuadmin, pk=user_id)
    budget = Annualbudget.objects.all()
    program = Program.objects.all()
    return render(request, 'admin_dashboard/admin_dashboard.html', {'budget': budget, 'admin': admin, 'program':program})

from decimal import Decimal

def budget(request):
    if request.method == 'POST':
        program_budget = request.POST.get('program_budget')
        budget_date = request.POST.get('budget_date')

        if not program_budget or not budget_date:
            return render(request, 'admin_dashboard/budget.html', {'error': 'All fields are required.'})

        parsed_date = datetime.datetime.strptime(budget_date, '%Y-%m-%d')
        year = parsed_date.year

        try:
            budget_entry = Annualbudget.objects.get(year=year)
            budget_entry.budget += Decimal(program_budget)
            budget_entry.save()
        except Annualbudget.DoesNotExist:
            Annualbudget.objects.create(budget=Decimal(program_budget), year=year)

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


def helper_filter(request):
    coordinators = User.objects.all()
    years = Annualbudget.objects.all()
    months = [month for month in calendar.month_name if month]
    projects = Program.objects.all()

    data = request.POST if request.method == 'POST' else request.GET

    project_name = data.get('project_name', '').strip()
    coord_filter = data.get('coordinator')
    year_filter = data.get('year', '').strip()
    quarter_filter = data.get('quarter', '').strip()
    month_filter = data.get('month', '').strip()
    sub_type_filter = data.get('sub_type', '').strip()


    if project_name:
        projects = projects.filter(title__icontains=project_name)

    if coord_filter:
        projects = projects.filter(coordinator__id=coord_filter)

    if year_filter:
        projects = projects.filter(annual_budget__year=year_filter)

    if sub_type_filter:
        projects = projects.filter(program_sub_type__iexact=sub_type_filter)

    if quarter_filter:
        quarter_map = {
            'Q1': (1, 3),
            'Q2': (4, 6),
            'Q3': (7, 9),
            'Q4': (10, 12),
        }
        if quarter_filter in quarter_map:
            start_month, end_month = quarter_map[quarter_filter]
            projects = projects.filter(
                created_at__month__gte=start_month,
                created_at__month__lte=end_month
            )

    if month_filter:
        try:
            month_index = list(calendar.month_name).index(month_filter)
            projects = projects.filter(created_at__month=month_index)
        except ValueError:
            pass
    
    total_budget = 0
    total_used_budget = 0
    total_budget_query = Annualbudget.objects.all()
    for y in total_budget_query:
        total_budget += y.budget

    for p in projects:
        total_used_budget += p.program_budget

    remaining_budget = total_budget - total_used_budget

    return coordinators, years, months, projects, total_used_budget, remaining_budget

def view_projects(request):
    coordinators, years, months, projects, total_used_budget, remaining_budget = helper_filter(request)
    

    return render(request, 'admin_dashboard/view_projects.html', {
        'coordinators': coordinators,
        'years': years,
        'months': months,
        'projects': projects, 
        'total_used_budget':total_used_budget,
        'remaining_budget':remaining_budget,
    })

def export_projects_excel(request):
    _, _, _, projects, total_used_budget, remaining_budget = helper_filter(request)

    wb = Workbook()
    ws = wb.active
    ws.title = "Projects"

    ws.append(["Title", "Coordinator", "Year", "Created At", "Budget", "Sub-Type"])
    for p in projects:
        ws.append([
            p.title,
            p.coordinator.username,
            p.annual_budget.year if p.annual_budget else '',
            p.created_at.strftime('%Y-%m-%d'),
            p.program_budget,
            p.program_sub_type,
        ])
    ws.append(["Used Budget", total_used_budget])
    ws.append(["Remaining Budget", remaining_budget])

    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = 'attachment; filename="projects.xlsx"'
    wb.save(response)
    return response


from django.contrib import messages
from django.shortcuts import redirect

def export_projects_pdf(request, project_id):
    if not Projectreport.objects.filter(program_id=project_id).exists():
        messages.error(request, "Report does not exist for this program.")
        return redirect('view_projects') 
    
    program = get_object_or_404(Program, pk=project_id)
    project_report = Projectreport.objects.get(program_id=project_id)

    template = get_template('admin_dashboard/project_pdf.html')
    html = template.render({'project_report': project_report, 'program_type': program.type})
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{program.title}-report.pdf"'
    
    pisa.CreatePDF(html, dest=response)
    return response


def edit_project(request, project_id):
    project = get_object_or_404(Program, id=project_id)
    users = User.objects.all()

    if request.method == 'POST':
        project.type = request.POST.get('program_type')
        project.title = request.POST.get('program_title')
        project.coordinator_id = request.POST.get('program_coordinator')
        project.program_budget = request.POST.get('program_budget')
        project.program_sub_type = request.POST.get('program_sub_type')
        project.save()
        return redirect('view_projects')

    return render(request, 'admin_dashboard/projects.html', {
        'users': users,
        'edit_mode': True,
        'project': project
    })


def delete_project(request, project_id):
    project = get_object_or_404(Program, id=project_id)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project deleted successfully.")
        return redirect('view_projects')

    return render(request, 'admin_dashboard/confirm_delete.html', {'project': project})
