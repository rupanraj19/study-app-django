from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from datetime import datetime

def daily_tasks(request):
    # Retrieve all tasks initially
    tasks = Task.objects.all()

    # Handle filtering by date
    filter_date = request.GET.get("filter_date")
    if filter_date:
        selected_date = datetime.strptime(filter_date, "%Y-%m-%d").date()
        tasks = [task for task in tasks if task.date.date() == selected_date]

    # Handle adding a new task
    if request.method == "POST":
        task_name = request.POST.get("task")
        if task_name:
            Task.objects.create(task=task_name, date=datetime.now())
        return redirect("daily_tasks")

    context = {
        "tasks": tasks,
    }
    return render(request, "index.html", context)

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("daily_tasks")

def mark_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = "Completed"
    task.save()
    return redirect("daily_tasks")

def mark_pending(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = "Pending"
    task.save()
    return redirect("daily_tasks")
