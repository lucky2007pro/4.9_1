from django.db import models

# Create your models here.
class Computer(models.Model):
    year = models.IntegerField(default=2024)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    videocard = models.CharField(max_length=100)
    ram = models.IntegerField()
    cpu = models.CharField(max_length=100)
    disk = models.IntegerField()
    monitor = models.CharField(max_length=100)
    price = models.IntegerField()
    def __str__(self):
        return f'{self.brand} {self.model}'