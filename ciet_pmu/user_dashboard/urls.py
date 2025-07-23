from django.urls import path
from . import views

urlpatterns = [
    # path('<int:user_id>/user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('<int:program_id>/edit_program/', views.edit_program, name='edit_program'),
    # path('save_program_details/', views.save_program_details, name='save_program_details'),
]
