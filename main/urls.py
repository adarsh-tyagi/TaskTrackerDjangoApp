from django.urls import path
from . import views

app_name = "main"

# urls for main application
urlpatterns = [
    path("", views.home, name="home") ,
    path("register/", views.register, name="register"),
    path("login/", views.loginuser, name="loginuser"),
    path("logout/", views.logoutuser, name="logoutuser"),
    path('create/', views.createtask, name="createtask"),
    path('tasks/', views.currenttasks, name='currenttasks'),
    path('task/<int:task_pk>/complete/', views.completetask, name="completetask"),
    path('task/<int:task_pk>/delete/', views.deletetask, name="deletetask")
]
