from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class ClothingItem(models.Model):
    CATEGORY_CHOICES = [
        ('TOP', 'Top'),
        ('BOTTOM', 'Bottom'),
        ('FOOTWEAR', 'Footwear'),
        ('OUTERWEAR', 'Outerwear'),
        ('ACCESSORY', 'Accessory'),
    ]

    MATERIAL_CHOICES = [
        ('COTTON', 'Cotton'),
        ('WOOL', 'Wool'),
        ('SYNTHETIC', 'Synthetic'),
        ('LEATHER', 'Leather'),
        ('LINEN', 'Linen'),
        ('POLYESTER', 'Polyester'),
        ('R-POLYESTER', 'Recycled Polyester'),
        ('LYOCELL', 'Lyocell/Organic Cotton'),
        ('MODAL', 'Modal'),
        ('NYLON', 'Nylon'),
        ('DENIM', 'Denim'),
        ('SPANDEX', 'Spandex'),
        ('BAMBOO', 'Bamboo'),
        ('ACRYLIC', 'Acrylic'),


    ]

    name = models.CharField(max_length=100)
    second_hand = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES, blank=True, null=True)
    colour = models.CharField(max_length=30, blank=True, null=True)
    size = models.CharField(max_length=10, blank=True, null=True)
    purchase_date = models.DateField()
    date_added = models.DateField(default=timezone.now)
    last_worn_date = models.DateField(blank=True, null=True)
    worn_count = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    sustainable_material = models.BooleanField(default=False, help_text="Is the material sustainable?")
    description = models.TextField(blank=True, null=True, help_text="Any additional notes about the item")
    image = models.ImageField(upload_to='clothing_items/', blank=True, null=True)
    wash_count = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.name

    def wear(self):
        """A method to increment the worn count and update last_worn_date."""
        self.worn_count += 1
        self.last_worn_date = timezone.now()
        self.save()
    
    def wash(self):
        """A method to increment the wash count """
        self.wash_count += 1
        self.save()
