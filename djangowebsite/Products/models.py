from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    summary = models.TextField(blank=True)
    featured = models.BooleanField(default=False);

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})