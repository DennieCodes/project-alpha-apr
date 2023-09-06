from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from tasks.forms import TaskForm


# SHOW_MY_TASKS
@login_required
def show_my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)

    context = {
        "tasks": tasks,
    }

    return render(request, "tasks/my_list.html", context)


# CREATE TASK
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(False)
            task.assignee = request.user
            task.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }

    return render(request, "tasks/create.html", context)
