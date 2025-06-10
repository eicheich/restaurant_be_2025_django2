from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from ..models import MenuCategory, MenuItem
from ..serializers.menu_serializers import (
    MenuCategorySerializer,
    MenuItemSerializer,
    MenuItemDetailSerializer
)


class MenuCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for menu categories
    """
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']


class MenuItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for menu items
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['name', 'price', 'created_at']
    ordering = ['name']

    def get_serializer_class(self):
        """
        Return appropriate serializer class based on the action
        """
        if self.action == 'retrieve':
            return MenuItemDetailSerializer
        return super().get_serializer_class()

    @action(detail=False, methods=['get'], url_path='category/(?P<category_id>[^/.]+)')
    def by_category(self, request, category_id=None):
        """
        Get items by category ID
        """
        try:
            items = self.get_queryset().filter(category_id=category_id)
            serializer = self.get_serializer(items, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
