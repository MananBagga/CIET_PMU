from django.shortcuts import render, get_object_or_404
from admin_dashboard.models import Program, User
from django.contrib.auth.decorators import login_required


def user_dashboard(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    programs = Program.objects.filter(coordinator_id=user.id)
    return render(request, 'user_dashboard/user_dashboard.html', {
        'user': user,
        'programs': programs
    })
