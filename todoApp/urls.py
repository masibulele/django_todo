from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginn,name='login'),
    path('register',views.signup, name='register'),
    path('home', views.home,name='home'),
    path('logout', views.log_out, name='logout'),
    path('add', views.add_task, name="add"),
    path('delete/<int:id>', views.remove_task, name="del"),
    path('edit/<int:id>', views.edit_task, name="edit"),

]