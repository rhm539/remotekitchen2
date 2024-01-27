from django.db import models
from django.db import models
from Restaurant.models import MenuItem
from accounts.models import CustomUser

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    # Add other order details

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_token = models.CharField(max_length=255)  # Assuming using Stripe tokens
    status = models.CharField(max_length=20)  # Success, Failed, Pending, etc.
    # Add other payment details
