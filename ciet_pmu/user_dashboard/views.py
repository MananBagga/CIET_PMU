from django.shortcuts import render, get_object_or_404, redirect
from admin_dashboard.models import Program, User, Subentry

def user_dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    user = get_object_or_404(User, pk=user_id)
    programs = Program.objects.filter(coordinator_id=user.id)
    subtask = Subentry.objects.all()
    return render(request, 'user_dashboard/user_dashboard.html', {
        'user': user,
        'programs': programs, 
        'subtask':subtask
    })

def edit_program(request, program_id):
    program = get_object_or_404(Program, pk=program_id)

    if request.method == 'POST':
        kpi_names = request.POST.getlist('kpi_name[]')
        kpi_dates = request.POST.getlist('kpi_date[]')
        kpi_budgets = request.POST.getlist('kpi_budget[]')

        workshop_names = request.POST.getlist('workshop_name[]')
        workshop_dates = request.POST.getlist('workshop_date[]')
        workshop_budgets = request.POST.getlist('workshop_budget[]')

        meetings_names = request.POST.getlist('meeting_name[]')
        meetings_dates = request.POST.getlist('meeting_date[]')
        meetings_budgets = request.POST.getlist('meeting_budget[]')

        manpower_names = request.POST.getlist('manpower_details[]')
        manpower_dates = request.POST.getlist('manpower_date[]')
        manpower_budgets = request.POST.getlist('manpower_budget[]')

        for name, date, budget in zip(kpi_names, kpi_dates, kpi_budgets):
            Subentry.objects.create(
                program_id=program_id,
                program=program,
                subtask="kpi",
                subtask_name=name,
                subtask_date=date,
                subtask_budget=budget
            )
        for name, date, budget in zip(workshop_names, workshop_dates, workshop_budgets):
            Subentry.objects.create(
                program_id=program_id,
                program=program,
                subtask="workshop",
                subtask_name=name,
                subtask_date=date,
                subtask_budget=budget
            )
        for name, date, budget in zip(meetings_names, meetings_dates, meetings_budgets):
            Subentry.objects.create(
                program_id=program_id,
                program=program,
                subtask="meetings",
                subtask_name=name,
                subtask_date=date,
                subtask_budget=budget
            )
        for name, date, budget in zip(manpower_names, manpower_dates, manpower_budgets):
            Subentry.objects.create(
                program_id=program_id,
                program=program,
                subtask="manpower",
                subtask_name=name,
                subtask_date=date,
                subtask_budget=budget
            )

        # return redirect('program_detail', program_id=program.id)


    return render(request, 'user_dashboard/edit_program.html', {'program': program})


# def update_program(request, program_id):
#     program = get_object_or_404(Program, pk=program_id)

#     if request.method == 'POST':
#         kpi_names = request.POST.getlist('kpi_name[]')
#         kpi_dates = request.POST.getlist('kpi_date[]')
#         kpi_budgets = request.POST.getlist('kpi_budget[]')

#         workshop_names = request.POST.getlist('workshop_name[]')
#         workshop_dates = request.POST.getlist('workshop_date[]')
#         workshop_budgets = request.POST.getlist('workshop_budget[]')

#         meetings_names = request.POST.getlist('meeting_name[]')
#         meetings_dates = request.POST.getlist('meeting_date[]')
#         meetings_budgets = request.POST.getlist('meeting_budget[]')

#         manpower_names = request.POST.getlist('manpower_details[]')
#         manpower_dates = request.POST.getlist('manpower_date[]')
#         manpower_budgets = request.POST.getlist('manpower_budget[]')

#         for name, date, budget in zip(kpi_names, kpi_dates, kpi_budgets):
#             Subentry.save()
#         for name, date, budget in zip(workshop_names, workshop_dates, workshop_budgets):
#             Subentry.save()
#         for name, date, budget in zip(meetings_names, meetings_dates, meetings_budgets):
#             Subentry.save()
#         for name, date, budget in zip(manpower_names, manpower_dates, manpower_budgets):
#             Subentry.save()

#         # return redirect('program_detail', program_id=program.id)


#     return render(request, 'user_dashboard/edit_program.html', {'program': program, 'update_mode':True})