from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ("name",)

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="item_images")
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return f"{self.name}: ${self.price}"
