from django.db import models
from django.urls import reverse


class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product-detail", args=[self.id])
