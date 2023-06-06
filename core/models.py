from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Books(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    publisher = models.CharField(max_length=100)
    published_date = models.DateField()
    distribution_expense = models.DecimalField(max_digits=2, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
