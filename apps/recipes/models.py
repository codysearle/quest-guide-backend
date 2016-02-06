from django.db import models


class Monster(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Quest(models.Model):
    name = models.CharField(max_length=100)
    objective = models.CharField(max_length=100, blank=True, null=True, help_text="Main Quest Objective")
    subquest = models.CharField(max_length=100, help_text="Subquest Requirements")
    monsters = models.ManyToManyField(Monster, blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    location = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return self.name
