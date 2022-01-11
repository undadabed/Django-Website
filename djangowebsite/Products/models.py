from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    summary = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    display_image = models.ImageField(null=True, blank=True, default='default.jpg')
    seller = models.ForeignKey(User, on_delete=CASCADE, default=1)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})

class OrderItem(models.Model):
    STATUS = (('Pending','Pending'),('Out for delivery','Out for delivery'),('Delivered','Delivered'))
    customer = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Cart():
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    total_price = models.IntegerField()