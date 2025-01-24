from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.daily_tasks, name="daily_tasks"),
    path("delete_task/<int:task_id>/", views.delete_task, name="delete_task"),
    path("mark_completed/<int:task_id>/", views.mark_completed, name="mark_completed"),
    path("mark_pending/<int:task_id>/", views.mark_pending, name="mark_pending"),
]
