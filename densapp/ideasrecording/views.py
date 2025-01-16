from rest_framework import mixins
from rest_framework.generics import GenericAPIView, ListAPIView
from .serializers import IdeaSerializer, ProjectSerializer
from .models import Idea, Project
from rest_framework.response import Response
from .sanitizers import sanitize_html
from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery, SearchHeadline
from .serializers import IdeaSearchSerializer



class CreateListIdea(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):

    serializer_class = IdeaSerializer
    
    def get_queryset(self):
        project_id = self.kwargs.get('project')
        return Idea.objects.filter(project__pk=project_id)
    
    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs['project'])
        sanitized_content = sanitize_html(self.request.data.get('content', ''))
        serializer.save(project=project, content=sanitized_content)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response([])
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        request.data['project'] = request.data.get('project_id')
        return self.create(request, *args, **kwargs)

class RetrieveUpdateDeleteIdea(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView
):

    serializer_class = IdeaSerializer
    queryset = Idea.objects.all()
    lookup_field = 'unique_id'

    def perform_update(self, serializer):
        sanitized_content = sanitize_html(self.request.data.get('content', ''))
        serializer.save(content=sanitized_content)

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
            return Response([])
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
        return self.destroy(request, *args, **kwargs)
    
class IdeaSearchView(ListAPIView):
    serializer_class = IdeaSearchSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        category = self.request.query_params.get('category', None)

        if not query:
            return Idea.objects.none()
        
        processed_query = ' & '.join(word + ':*' for word in query.split())
        
        vector = SearchVector('content', weight='A')
        search_query = SearchQuery(processed_query, search_type='raw')

        queryset = Idea.objects.select_related('project').annotate(
            rank=SearchRank(vector, search_query),
            highlighted_content=SearchHeadline(
                'content',
                search_query,
                start_sel='<mark>',
                stop_sel='</mark>',
                max_fragments=2,
            )
        ).filter(
            rank__gte=0.1
        ).order_by('-rank', '-created_at')

        if category:
            queryset = queryset.filter(category=category)

        return queryset