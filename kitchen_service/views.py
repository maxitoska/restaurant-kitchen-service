from django.shortcuts import render
from django.views import generic

from kitchen_service.models import DishType, Cook, Ingredient, Dish


def index(request):
    """View function for the home page of the site."""

    num_dish_types = DishType.objects.count()
    num_cooks = Cook.objects.count()
    num_ingredients = Ingredient.objects.count()
    num_dishes = Dish.objects.count()

    context = {
        "num_dish_types": num_dish_types,
        "num_cooks": num_cooks,
        "num_ingredients": num_ingredients,
        "num_dishes": num_dishes,
    }

    return render(request, "kitchen_service/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    queryset = DishType.objects.order_by("name")
    paginate_by = 5


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5


class CooksDetailView(generic.DetailView):
    model = Cook
    paginate_by = 5


class IngredientListView(generic.ListView):
    model = Ingredient
    paginate_by = 5


class IngredientDetailView(generic.DetailView):
    model = Ingredient
    paginate_by = 5


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5


class DishDetailView(generic.DetailView):
    model = Dish
    paginate_by = 5
