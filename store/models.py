from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     details = models.TextField()
#     image = models.ImageField(upload_to='category_images/')

#     def __str__(self):
#         return self.name

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     details = models.TextField()
#     image = models.ImageField(upload_to='product_images/')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
