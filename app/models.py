from django.db import models

class Truck(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cylinder = models.IntegerField()
    max_weight = models.IntegerField()
    max_speed = models.IntegerField()

    def __str__(self):
        return f'{self.title} is {self.max_weight} at max weight'