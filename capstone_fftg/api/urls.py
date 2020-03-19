from django.urls import include, path

from .views import CategoryViewSet, TechniqueViewSet, KeyWordViewSet, RecipeViewSet, IngredientsViewSet, CommentsViewSet

from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from . import views

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('techniques', TechniqueViewSet, basename='techniques')
router.register('keywords', KeyWordViewSet, basename='keywords')
router.register('ingredients', IngredientsViewSet, basename='ingredients')
router.register('comments', CommentsViewSet, basename='comments')
router.register('recipes', RecipeViewSet, basename='recipes')
router.register('users', views.UserViewSet, basename='users')
urlpatterns = router.urls


urlpatterns = [
    path('',include(router.urls)),
    # path('favorite/<int:id>',views.add_favorite)
    
]


