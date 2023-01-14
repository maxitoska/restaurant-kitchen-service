from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen_service.forms import (
    CookCreationForm,
    DishTypeSearchForm,
    IngredientSearchForm,
    DishSearchForm,
    CookSearchForm,
)
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishTypeSearchForm(initial={"name": name})

        return context

    def get_queryset(self):
        name = self.request.GET.get("name")

        if name:
            return self.queryset.filter(name__icontains=name)

        return self.queryset


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen_service:dish-type-list")
    template_name = "kitchen_service/dish_type_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen_service:dish-type-list")
    template_name = "kitchen_service/dish_type_form.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen_service:dish-type-list")
    template_name = "kitchen_service/dish_type_confirm_delete.html"


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5
    template_name = "kitchen_service/cook_list.html"
    queryset = get_user_model().objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = CookSearchForm(initial={"username": username})

        return context

    def get_queryset(self):
        username = self.request.GET.get("username")

        if username:
            return self.queryset.filter(username__icontains=username)

        return self.queryset


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("kitchen_service:cook-list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("kitchen_service:cook-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen_service:cook-list")
    template_name = "kitchen_service/cook_confirm_delete.html"


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    paginate_by = 5
    template_name = "kitchen_service/cook_detail.html"


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    paginate_by = 5
    template_name = "kitchen_service/ingredient_list.html"
    queryset = Ingredient.objects.order_by("name")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IngredientListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = IngredientSearchForm(initial={"name": name})

        return context

    def get_queryset(self):
        name = self.request.GET.get("name")

        if name:
            return self.queryset.filter(name__icontains=name)

        return self.queryset


class IngredientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Ingredient
    paginate_by = 5
    template_name = "kitchen_service/ingredient_detail.html"


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen_service:ingredient-list")


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen_service:ingredient-list")


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("kitchen_service:ingredient-list")
    template_name = "kitchen_service/ingredient_confirm_delete.html"


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5
    template_name = "kitchen_service/dish_list.html"
    queryset = Dish.objects.all().order_by("name")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishSearchForm(initial={"name": name})

        return context

    def get_queryset(self):
        name = self.request.GET.get("name")

        if name:
            return self.queryset.filter(name__icontains=name)

        return self.queryset


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen_service:dish-list")


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    paginate_by = 5
    template_name = "kitchen_service/dish_detail.html"


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen_service:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen_service:dish-list")
    template_name = "kitchen_service/dish_confirm_delete.html"
