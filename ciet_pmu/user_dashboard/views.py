from django.shortcuts import render

# Create your views here.
def user_dashboard(request):

    program_type = request.session.get('program_type')
    program_sub_type = request.session.get('program_sub_type')
    program_title = request.session.get('program_title')
    program_budget = request.session.get('program_budget')

    context = {
        'program_type_name': program_type,
        'program_sub_type': program_sub_type,
        'program_title': program_title,
        'program_budget': program_budget
    }

    return render(request, 'user_dashboard/user_dashboard.html', context)