from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

    class Meta:
        app_label = "api"
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

    class Meta:
        app_label = "api"
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        app_label = "api"
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return f"{self.product.name} - {self.category.name}"
