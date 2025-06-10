from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from ..models import Article
from ..serializers.article_serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint for articles
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'  # Use slug for lookups instead of ID
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['title', 'created_at']
    ordering = ['-created_at']  # Default ordering: newest first

    # Override to support both slug and ID lookups
    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        lookup_value = self.kwargs[lookup_url_kwarg]

        # Try to get by slug first
        queryset = self.filter_queryset(self.get_queryset())

        # If lookup value is numeric, try by ID
        if lookup_value.isdigit():
            obj = queryset.filter(id=lookup_value).first()
            if obj:
                self.check_object_permissions(self.request, obj)
                return obj

        # Otherwise use the default lookup (by slug)
        return super().get_object()
