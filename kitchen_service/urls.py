from django.urls import path

from kitchen_service.views import (
    index,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    CookListView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    CookDetailView,
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
        "dish_types/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),
    path(
        "dish_types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dish_types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),

    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list",
    ),
    path(
        "cooks/create/",
        CookCreateView.as_view(),
        name="cook-create",
    ),

    path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail",
    ),
    path(
        "cooks/<int:pk>/update/",
        CookUpdateView.as_view(),
        name="cook-update",
    ),
    path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete",
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
