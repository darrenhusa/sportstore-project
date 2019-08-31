from django.db import models

# Create your models here.
class Product(models.Model):
    """Model representing a product."""
    name = models.CharField(max_length=50, help_text='Enter the product name.')
    description = models.CharField(max_length=100, help_text='Enter the product description.')
    price = models.DecimalField(max_digits=5, decimal_places=2, help_text='Enter the product price.')
    category = models.CharField(max_length=50, help_text='Enter the product category.')

    def __str__(self):
        """String for representing the Model object."""
        return self.name
