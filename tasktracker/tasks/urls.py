from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('done/', views.task_list_done, name='task_list_done'),
    path('todo/', views.task_list_todo, name='task_list_todo'),
    path('in-progress/', views.task_list_in_progress, name='task_list_in_progress'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('mark-in-progress/<int:pk>/', views.task_mark_in_progress, name='task_mark_in_progress'),
    path('mark-done/<int:pk>/', views.task_mark_done, name='task_mark_done'),
]