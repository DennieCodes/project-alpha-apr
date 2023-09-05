from django.shortcuts import render
from projects.models import Project


def list_projects(request):
    projects = Project.objects.all()

    context = {"projects": projects}

    return render(request, "projects/list.html", context)
