from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.CreateListProject.as_view()),
    path('projects/<uuid:pk>', views.RetrieveUpdateDeleteProject.as_view()),
    path('ideas/<uuid:project>', views.CreateListIdea.as_view()),
    path('ideas/', views.RetrieveUpdateDeleteIdea.as_view()),
]

