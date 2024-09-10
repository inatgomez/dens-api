from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.CreateListProject.as_view()),
    path('projects/', views.RetrieveUpdateDeleteProject.as_view()),
    path('ideas/<int:project>', views.CreateListIdea.as_view()),
    path('ideas/', views.CreateIdea.as_view()),
    path('ideas/', views.RetrieveUpdateDeleteIdea.as_view()),
]

