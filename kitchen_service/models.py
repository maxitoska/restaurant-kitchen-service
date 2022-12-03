from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(unique=True, default=0)

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def get_absolute_url(self):
        return reverse("kitchen_service:cook-detail", args=[str(self.id)])


class Ingredient(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return {self.name}

    def get_absolute_url(self):
        return reverse("kitchen_service:ingredient-detail", args=[str(self.id)])


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.FloatField()
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="dishes")
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes_ingredient")

    def __str__(self):
        return f"{self.name} {self.description} {self.price} {self.dish_type}"

    def get_absolute_url(self):
        return reverse("kitchen_service:dish-detail", args=[str(self.id)])
