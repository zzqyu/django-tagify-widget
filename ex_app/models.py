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
    name = models.CharField(max_length=50);
    category = models.ForeignKey(
        Type,
        on_delete=models.CASCADE
    )
    makers = models.ManyToManyField(Maker)

    def __str__(self) -> str:
        return self.name
