from django.db import models

# Create your models here.
class Laptop(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    videocard = models.CharField(max_length=100)
    year = models.IntegerField(default=2026)
    ram = models.IntegerField()
    cpu = models.IntegerField()
    disk = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return f'{self.brand} {self.model}'