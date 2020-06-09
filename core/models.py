from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from django.core.validators import RegexValidator

CATEGORY_CHOISES = (
    ('0', 'הכל'),
    ('A','מוצרי נייר'),
    ('B','מוצרי אלומיניום'),
    ('C','מוצרי קרטון'),
    ('D','מוצרי פלסטיק'),
    ('E','מוצרי ניילון'),
    ('F','קופסאות פלסטיק'),
    ('G','חומרי ניקיון'),
    ('H','כוסות'),
    ('I','עזרי ניקיון'),
    ('J','מוצרי היגיינה'),
    ('K','סכינים וציוד מוסדי'),
    ('L','מוצרי עזר למוסכים'),
)



numeric = RegexValidator(r'^[0-9+]', 'Only digit characters.')

# Create your models here.
class Item(models.Model):
    barcode = models.CharField(primary_key=True, unique=True, max_length=128, validators=[numeric])
    title = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOISES,max_length=2)
    in_box = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={"pk": self.barcode})

    def get_add_to_cart_url(self):
        return reverse('core:add-to-cart', kwargs={'pk':self.barcode})

    def remove_from_cart_url(self):
        return reverse('core:remove-from-cart', kwargs={'pk':self.barcode})

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.item.title} - {self.quantity}'

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)