from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.menu_views import MenuCategoryViewSet, MenuItemViewSet
from .views.article_views import ArticleViewSet
from .views.upload_views import ImageUploadView

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'menu/categories', MenuCategoryViewSet)
router.register(r'menu/items', MenuItemViewSet)
router.register(r'articles', ArticleViewSet)

# URL patterns
urlpatterns = [
    path('', include(router.urls)),
    path('upload/image/', ImageUploadView.as_view(), name='upload-image'),
]
