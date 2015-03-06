from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Monster(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True, help_text="This is a quick description of your recipe")
    directions = models.TextField(help_text="How to make the recipe")
    ingredients = models.ManyToManyField(Ingredient)
    tags = models.ManyToManyField(Tag)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return self.name


class Quest(models.Model):
    name = models.CharField(max_length=100)
    objective = models.CharField(max_length=100, blank=True, null=True, help_text="Main Quest Objective")
    subquest = models.CharField(max_length=100, help_text="Subquest Requirements")
    monsters = models.ManyToManyField(Monster, blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return self.name