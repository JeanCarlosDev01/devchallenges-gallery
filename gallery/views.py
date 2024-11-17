from django.shortcuts import render
from add_project.models import Project


def index(request):
    project_list = Project.objects.all()
    context = {
        'project_list': project_list
    }
    return render(request, 'projects_gallery.html', context)
