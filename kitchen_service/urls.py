from django.urls import path

from kitchen_service.views import (
    index,
    DishTypeListView,
    CookListView,
    CooksDetailView,
    IngredientListView,
    IngredientDetailView,
    DishListView,
    DishDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "dish_types/",
        DishTypeListView.as_view(),
        name="dish-type-list",
    ),

    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list",
    ),

    path(
        "cooks/<int:pk>/",
        CooksDetailView.as_view(),
        name="cooks-detail",
    ),

    path(
        "ingredients/",
        IngredientListView.as_view(),
        name="ingredient-list",
    ),
    path(
        "ingredients/<int:pk>/",
        IngredientDetailView.as_view(),
        name="ingredient-detail",
    ),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list",
    ),

    path(
        "dish/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail",
    ),
]

app_name = "kitchen_service"
