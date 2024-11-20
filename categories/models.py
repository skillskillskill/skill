from django.db import models

# Create your models here.


class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name
