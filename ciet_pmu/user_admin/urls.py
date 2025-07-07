from django.urls import path
from .views import user_admin

urlpatterns = [
<<<<<<< HEAD
    path('user_admin/', user_admin, name='user_admin'),
]
=======
    path('', user_admin, name='user_admin'),
]
>>>>>>> 7ebaad400bd5dd141310415e70e97112c4cd6c9d
