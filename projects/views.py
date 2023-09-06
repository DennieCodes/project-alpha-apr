from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from projects.forms import ProjectForm
from django.contrib.auth.decorators import login_required


# CREATE_PROJECT
@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {
        "form": form,
    }

    return render(request, "projects/create.html", context)


# LIST_PROJECTS
@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)

    context = {"projects": projects}

    return render(request, "projects/list.html", context)


# SHOW_PROJECT
@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)

    context = {
        "project": project,
    }

    return render(request, "projects/detail.html", context)
