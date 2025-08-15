from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.task_create, name='task_create'),
    path('tasks/delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/toggle/', views.task_toggle, name='task_toggle'),
    path('tasks/<int:pk>/edit/', views.task_update, name='task_update'),
    path('logout/', auth_views.LogoutView.as_view(next_page='task_list'), name='logout'),
]
