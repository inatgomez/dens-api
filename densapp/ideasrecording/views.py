from django.http import JsonResponse
from django.core import serializers
from rest_framework.generics import ListCreateAPIView
from .models import Idea, Project

class list_projects(ListCreateAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# def list_projects(request):
#     projects = Project.objects.all()
#     data = [serializers.serialize('json', projects)]
#     return JsonResponse(data, safe=False)

# def list_ideas_in_project(request, project_id):
#     ideas = Idea.objects.filter(project_id=project_id)
#     data = [serializers.serialize('json', ideas)]
#     return JsonResponse(data, safe=False)