from django.urls import path

from . import views
from .views_register import register_user 

app_name="user"

urlpatterns = [
	path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('register', register_user, name ='register'),
    
]