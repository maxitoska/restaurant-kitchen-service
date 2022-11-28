from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(unique=True, default=0)

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)
    count = models.IntegerField()
    price = models.IntegerField()


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.IntegerField()
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="dishes")
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes")
