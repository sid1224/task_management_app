from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_tasks, name='task_list'),  # View all tasks
    path('create/', views.create_task, name='create_task'),  # Create a new task
    path('<int:task_id>/edit/', views.edit_task, name='edit_task'),  # Edit a specific task
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),  # Delete a specific task
]
