from rest_framework import serializers

from kitchen_service.models import (
    DishType,
    Cook,
    Dish,
    Ingredient,
)


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ("id", "name")


class DishTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishType
        fields = ("id", "name")


class CookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cook
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "years_of_experience"
        )


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = (
            "id",
            "name",
            "description",
            "price",
            "dish_type",
            "cooks",
            "ingredients",
        )
