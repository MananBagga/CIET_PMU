from django.shortcuts import render, get_object_or_404, redirect
from admin_dashboard.models import Program, User, Subentry
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

def save_entries(ids, names, dates, budgets, entry_type, program_id):
    program = Program.objects.get(pk=program_id) 
    for entry_id, name, date, budget in zip(ids, names, dates, budgets):
        if entry_id: 
            try:
                sub = Subentry.objects.get(id=entry_id)
                sub.subtask_name = name
                sub.subtask_date = date
                sub.subtask_budget = budget
                sub.save()
            except Subentry.DoesNotExist:
                pass
        else:  
            Subentry.objects.create(
                program=program,      
                subtask=entry_type,
                subtask_name=name,
                subtask_date=date,
                subtask_budget=budget
            )


def edit_program(request, program_id):
    program = get_object_or_404(Program, pk=program_id)

    if request.method == 'POST':
        kpi_ids = request.POST.getlist('kpi_id[]')
        kpi_names = request.POST.getlist('kpi_name[]')
        kpi_dates = request.POST.getlist('kpi_date[]')
        kpi_budgets = request.POST.getlist('kpi_budget[]')

        workshop_ids = request.POST.getlist('workshop_id[]')
        workshop_names = request.POST.getlist('workshop_name[]')
        workshop_dates = request.POST.getlist('workshop_date[]')
        workshop_budgets = request.POST.getlist('workshop_budget[]')

        meeting_ids = request.POST.getlist('meeting_id[]')
        meeting_names = request.POST.getlist('meeting_name[]')
        meeting_dates = request.POST.getlist('meeting_date[]')
        meeting_budgets = request.POST.getlist('meeting_budget[]')

        manpower_ids = request.POST.getlist('manpower_id[]')
        manpower_names = request.POST.getlist('manpower_details[]')
        manpower_dates = request.POST.getlist('manpower_date[]')
        manpower_budgets = request.POST.getlist('manpower_budget[]')

        save_entries(kpi_ids, kpi_names, kpi_dates, kpi_budgets, "kpi", program_id)
        save_entries(workshop_ids, workshop_names, workshop_dates, workshop_budgets, "workshop", program_id)
        save_entries(meeting_ids, meeting_names, meeting_dates, meeting_budgets, "meetings", program_id)
        save_entries(manpower_ids, manpower_names, manpower_dates, manpower_budgets, "manpower", program_id)

        return redirect('user_dashboard')


    kpi_entries = Subentry.objects.filter(program=program, subtask="kpi")
    workshop_entries = Subentry.objects.filter(program=program, subtask="workshop")
    meeting_entries = Subentry.objects.filter(program=program, subtask="meetings")
    manpower_entries = Subentry.objects.filter(program=program, subtask="manpower")

    return render(request, 'user_dashboard/edit_program.html', {
        'program': program,
        'kpi_entries': kpi_entries,
        'workshop_entries': workshop_entries,
        'meeting_entries': meeting_entries,
        'manpower_entries': manpower_entries,
    })
    


@csrf_exempt
def delete_subentry(request, entry_id):
    if request.method == "DELETE":
        try:
            Subentry.objects.get(id=entry_id).delete()
            return JsonResponse({"success": True})
        except Subentry.DoesNotExist:
            return JsonResponse({"success": False, "error": "Not found"})
    return JsonResponse({"success": False, "error": "Invalid request"})