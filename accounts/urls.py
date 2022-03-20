from django.urls import path
from . import views

urlpatterns = [
    path("login", views.loginuser, name="login"),
    path("register", views.createUser, name="createuser")
]
