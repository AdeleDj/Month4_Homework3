from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TourCompany(models.Model):
    name = models.CharField(max_length=100)
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.name


class Horse(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Rider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    horse = models.OneToOneField(Horse, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(TourCompany, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()

    def clean(self):
        if self.rating < 1 or self.rating > 5:
            raise ValidationError("Оценка только от 1 до 5")

    def __str__(self):
        return f"{self.user} -> {self.company} ({self.rating})"