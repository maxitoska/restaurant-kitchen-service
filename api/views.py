from rest_framework import viewsets

from kitchen_service.models import (
    DishType,
    Cook,
    Dish,
    Ingredient,
)

from api.serializers import (
    IngredientSerializer,
    DishTypeSerializer,
    CookSerializer,
    DishSerializer,
)


class DishTypeViewSet(viewsets.ModelViewSet):
    queryset = DishType.objects.all()
    serializer_class = DishTypeSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class CookViewSet(viewsets.ModelViewSet):
    queryset = Cook.objects.all()
    serializer_class = CookSerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
