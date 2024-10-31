from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    quantity = models.CharField(max_length=50, blank=False, null=False)
    size = models.CharField(max_length=50, blank=False, null=False)
    price = models.FloatField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.name