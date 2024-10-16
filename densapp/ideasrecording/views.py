from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from .serializers import IdeaSerializer, ProjectSerializer
from .models import Idea, Project
from rest_framework.response import Response

class CreateListIdea(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):

    serializer_class = IdeaSerializer
    queryset = Idea.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CreateIdea(mixins.CreateModelMixin, GenericAPIView):
    serializer_class = IdeaSerializer
    queryset = Idea.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RetrieveUpdateDeleteIdea(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView
):

    serializer_class = IdeaSerializer
    queryset = Idea.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        
class CreateListProject(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):

    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get(self, request, *args, **kwargs):
        projects = self.get_queryset()
        if not projects.exists():
            return Response([{"message": "You'll see your projects soon!"}])
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RetrieveUpdateDeleteProject(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView
):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, *kwargs)