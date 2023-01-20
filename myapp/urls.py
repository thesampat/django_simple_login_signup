from django.urls import path
from .views import *

urlpatterns = [
    path('home', view=home, name='home'),
    path('login', view=user_login, name='login'),
    path('signup', view=user_signup, name='signup'),
    path('handle_login', view=handle_login, name='handle_login'),
    path('handle_register', view=handle_signup, name='handle_register'),
]
