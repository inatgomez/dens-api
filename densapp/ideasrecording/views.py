from django.http import JsonResponse
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Idea, Project

@api_view(['POST'])
def record_idea(request):
    if request.method == 'POST':
        serializer = serializers.serialize(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def list_projects(request):
    projects = Project.objects.all()
    data = [serializers.serialize('json', projects)]
    return JsonResponse(data, safe=False)

def list_ideas_in_project(request, project_id):
    ideas = Idea.objects.filter(project_id=project_id)
    data = [serializers.serialize('json', ideas)]
    return JsonResponse(data, safe=False)