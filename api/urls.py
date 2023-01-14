from rest_framework import routers
from django.urls import path, include

from api.views import (
    DishViewSet,
    DishTypeViewSet,
    CookViewSet,
    IngredientViewSet,
)

router = routers.DefaultRouter()
router.register("cooks", CookViewSet)
router.register("dishes", DishViewSet)
router.register("dish_types", DishTypeViewSet)
router.register("ingredients", IngredientViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "api"
