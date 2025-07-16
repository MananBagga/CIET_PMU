from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/user_dashboard/', views.user_dashboard, name='user_dashboard')
    # path('user_dashboard/', views.user_dashboard, name='user_dashboard')
]
