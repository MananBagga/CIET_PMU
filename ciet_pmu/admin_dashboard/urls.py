from django.urls import path
from . import views

urlpatterns = [
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('budget/', views.budget, name='budget'),
    path('projects/', views.projects, name='projects'),
    path('view_projects/', views.view_projects, name='view_projects'),
    path('export/excel/', views.export_projects_excel, name='export_projects_excel'),
    path('export/pdf/', views.export_projects_pdf, name='export_projects_pdf'),
]