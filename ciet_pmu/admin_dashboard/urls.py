from django.urls import path
from . import views

urlpatterns = [
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('budget/', views.budget, name='budget'),
    path('projects/', views.projects, name='projects'),
    path('view_projects/', views.view_projects, name='view_projects'),
]