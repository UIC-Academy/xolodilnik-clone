from django.db import models

from common.models import BaseModel


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products")
    category = models.ForeignKey(
        "products.Category", on_delete=models.RESTRICT, related_name="products"
    )
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductVariant(BaseModel):
    product = models.ForeignKey(
        "products.Product", on_delete=models.RESTRICT, related_name="variants"
    )
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=255, null=True, blank=True)
    size = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.color} - {self.size}"


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
