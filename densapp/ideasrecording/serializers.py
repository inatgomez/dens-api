from rest_framework import serializers
from .models import Idea, Project

class IdeaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Idea
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"

