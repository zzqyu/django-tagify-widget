from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=10);

    def __str__(self) -> str:
        return self.name


class Maker(models.Model):
    name = models.CharField(max_length=20);

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    name = models.CharField(max_length=50);
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES);
    category = models.ForeignKey(
        Type,
        on_delete=models.CASCADE
    )
    makers = models.ManyToManyField(Maker)

    def __str__(self) -> str:
        return self.name
