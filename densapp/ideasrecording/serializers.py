from rest_framework import serializers
from .models import Idea, Project

class IdeaSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), source='project_id')
    class Meta:
        model = Idea
        fields = "__all__"
        read_only_fields = ('created_at', 'updated_at')

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ('created_at')

