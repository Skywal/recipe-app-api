"""
Filters for recipe APIs.
"""
from django_filters import rest_framework as filters

from core.models import Recipe


class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class RecipeFilter(filters.FilterSet):
    tags = NumberInFilter(field_name='tags__id', lookup_expr='in')
    ingredients = NumberInFilter(field_name='ingredients__id', lookup_expr='in')

    class Meta:
        model = Recipe
        fields = ['tags', 'ingredients']
