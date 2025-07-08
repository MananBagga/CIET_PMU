"""
URL configuration for ciet_pmu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('user_admin.urls')),
    path('', include('signup.urls')),
    path('', include('login.urls')),
    path('', include('admin_login.urls')),

    path('', include('admin_dashboard.urls')),

    path('', include('user_dashboard.urls')),


    path("__reload__/", include("django_browser_reload.urls")),
]














    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),