from django.urls import path
from .views import user_register, user_login,user_logout

urlpatterns = [
    path('user_register/', user_register, name='user_register'),
    path('user_login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'), 
]