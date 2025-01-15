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

class IdeaSearchSerializer(serializers.ModelSerializer):
    highlighted_content = serializers.CharField(read_only=True)
    rank = serializers.FloatField(read_only=True)
    preview_content = serializers.SerializerMethodField()

    class Meta:
        model = Idea
        fields = [
            'unique_id',
            'preview_content',
            'highlighted_content',
            'category',
            'created_at',
            'rank'
        ]
    
    def get_preview_content(self, obj):
        """Returns first 100 characters of the content as preview"""
        return obj.content[:100] + ('...' if len(obj.content) > 100 else '')