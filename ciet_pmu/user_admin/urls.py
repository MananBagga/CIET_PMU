from django.urls import path
from .views import user_admin

urlpatterns = [
    path('user_admin/', user_admin, name='user_admin'),
]
