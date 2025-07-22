from django.shortcuts import render, redirect, get_object_or_404
import datetime
import calendar
from .models import User, Program, Annualbudget, Pmuadmin

# Create your views here.
def admin_dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('admin_login')

    admin = get_object_or_404(Pmuadmin, pk=user_id)
    budget = Annualbudget.objects.all()
    return render(request, 'admin_dashboard/admin_dashboard.html', {'budget': budget, 'admin': admin})

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


def view_projects(request):
    coordinators = User.objects.all()
    years = Annualbudget.objects.all()
    months = [month for month in calendar.month_name if month]

    projects = Program.objects.all()  

    if request.method == 'POST':
        project_name = request.POST.get('project_name', '').strip()
        coord_filter = request.POST.get('coordinator')
        year_filter = request.POST.get('year', '').strip()
        quarter_filter = request.POST.get('quarter', '').strip()
        month_filter = request.POST.get('month', '').strip()
        period_filter = request.POST.get('period', '').strip()

        coord_filter = User.objects.filter(username = coord_filter).id

        if project_name:
            projects = projects.filter(title=project_name)

        if coord_filter:
            projects = projects.filter(coordinator_id=coord_filter)

        if year_filter:
            projects = projects.filter(annual_budget__year=year_filter)

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
                    annual_budget__year__isnull=False,  # Ensure year exists
                    created_at__month__gte=start_month,
                    created_at__month__lte=end_month
                )

        if month_filter:
            try:
                month_index = list(calendar.month_name).index(month_filter)
                projects = projects.filter(created_at__month=month_index)
            except ValueError:
                pass  # Invalid month name

        # Optional: If you want to add more filtering by period (custom logic), add here

    return render(request, 'admin_dashboard/view_projects.html', {
        'coordinators': coordinators,
        'years': years,
        'months': months,
        'projects': projects,  
    })
