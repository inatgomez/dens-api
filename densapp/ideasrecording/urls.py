from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.list_projects, name='list_projects'),
    path('ideas/<int:project_id>', views.list_ideas_in_project, name='list_ideas_in_project'),
]