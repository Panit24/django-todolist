from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/', views.get_all_tasks, name='get_all_tasks'),
    path('tasks/update/<task_id>/', views.update_task, name='update_task'),
    path('tasks/delete/<task_id>/', views.delete_task, name='delete_task'),
]
