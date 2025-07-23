from django.shortcuts import render, get_object_or_404, redirect
from admin_dashboard.models import Program, User

def user_dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    user = get_object_or_404(User, pk=user_id)
    programs = Program.objects.filter(coordinator_id=user.id)
    return render(request, 'user_dashboard/user_dashboard.html', {
        'user': user,
        'programs': programs
    })

def edit_program(request, program_id):
    # New view to handle the edit form page
    program = Program.objects.get(id=program_id)
    return render(request, 'user_dashboard/edit_program.html', {'program': program})
    # return render(request, 'user_dashboard/edit_program.html')
# from django.shortcuts import render, redirect
# from admin_dashboard.models import Program

# def user_dashboard(request, user_id):
#     # Fetch programs for the user based on user_id
#     programs = Program.objects.filter(user_id=user_id)  # Adjust based on your user model
#     return render(request, 'layout.html', {'programs': programs})


# def save_program_details(request):
#     # Existing save_program_details view
#     if request.method == 'POST':
#         program_id = request.POST['program_id']
#         program = Program.objects.get(id=program_id)
        
#         # Save KPI Details
#         KPIDetails.objects.update_or_create(
#             program=program,
#             defaults={
#                 'kpi_name': request.POST['kpi_name'],
#                 'kpi_date': request.POST['kpi_date'],
#                 'kpi_budget': request.POST['kpi_budget']
#             }
#         )
        
#         # Save Workshop Details
#         WorkshopDetails.objects.update_or_create(
#             program=program,
#             defaults={
#                 'workshop_name': request.POST['workshop_name'],
#                 'workshop_date': request.POST['workshop_date'],
#                 'workshop_budget': request.POST['workshop_budget']
#             }
#         )
        
#         # Save Meeting Details
#         MeetingDetails.objects.update_or_create(
#             program=program,
#             defaults={
#                 'meeting_name': request.POST['meeting_name'],
#                 'meeting_date': request.POST['meeting_date'],
#                 'meeting_budget': request.POST['meeting_budget']
#             }
#         )
        
#         # Save Manpower Details
#         ManpowerDetails.objects.update_or_create(
#             program=program,
#             defaults={
#                 'manpower_details': request.POST['manpower_details'],
#                 'manpower_date': request.POST['manpower_date'],
#                 'manpower_budget': request.POST['manpower_budget']
#             }
#         )
        
#         return redirect('user_dashboard', user_id=request.user.id)  # Redirect with user_id
#     return render(request, 'layout.html')
