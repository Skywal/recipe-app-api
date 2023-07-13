"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include
)

from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)
router.register('tags-no-mixin', views.TagNoMixViewSet)
router.register('ingredients-no-mixin', views.IngredientNoMixViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
