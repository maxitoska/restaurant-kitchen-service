from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from kitchen_service.models import DishType, Cook, Ingredient, Dish


def index(request):
    """View function for the home page of the site."""

    num_dish_types = DishType.objects.count()
    num_cooks = Cook.objects.count()
    num_ingredients = Ingredient.objects.count()
    num_dishes = Dish.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_dish_types": num_dish_types,
        "num_cooks": num_cooks,
        "num_ingredients": num_ingredients,
        "num_dishes": num_dishes,
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen_service/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    queryset = DishType.objects.order_by("name")
    template_name = "kitchen_service/dish_type_list.html"
    paginate_by = 5


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5
    template_name = "kitchen_service/cook_list.html"


class CooksDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    paginate_by = 5
    template_name = "kitchen_service/cook_detail.html"


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    paginate_by = 5
    template_name = "kitchen_service/ingredient_list.html"


class IngredientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Ingredient
    paginate_by = 5
    template_name = "kitchen_service/ingredient_detail.html"


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5
    template_name = "kitchen_service/dish_list.html"


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    paginate_by = 5
    template_name = "kitchen_service/dish_detail.html"
