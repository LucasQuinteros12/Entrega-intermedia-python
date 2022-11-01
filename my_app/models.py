from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=20)
    model = models.IntegerField()

    def __str__(self):
        return f"{self.brand} | {self.model}"

class Accesory(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    price = models.IntegerField(max_length=20)

    def __str__(self):
        return f"{self.name} | {self.type} | {self.price}"

class Clothe(models.Model):
    brand = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    size = models.IntegerField(max_length=20)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.brand} | {self.type} | {self.size} | {self.color}"
