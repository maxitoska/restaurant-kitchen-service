"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
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
        "ingredient/<int:pk>/",
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

