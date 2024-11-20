from rest_framework import serializers
from .models import Idea, Project

class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = "__all__"
        read_only_fields = ('created_at', 'updated_at')

    def validate_content(self, value):
        if len(value) > 2000:
            raise serializers.ValidationError("Content cannot exceed 2000 characters.")
        return value

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"

