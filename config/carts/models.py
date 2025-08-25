from django.db import models
from django.contrib.auth import get_user_model
from books.models import Book
import uuid

User = get_user_model()

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.user.get_full_name}"



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.book.title} x {self.quantity}"
    
    def total_price(self):
        return self.book.price * self.quantity
        


class Order(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("failed", "Failed")
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), unique=True)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, related_name='order')
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default="pending")
    invoice_number = models.CharField(max_length=6, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    created_time = models.DateField(auto_now=True)


    def __str__(self):
        return f"Oredr {self.id} - {self.cart.user} ({self.status})"