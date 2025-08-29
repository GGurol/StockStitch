from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    ITEM_TYPE_CHOICES = [
        ('stitched', 'Stitched'),
        ('unstitched', 'Unstitched'),
    ]
    item_name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=20, choices=ITEM_TYPE_CHOICES)
    fabric_type = models.CharField(max_length=100)
    cost_per_meter = models.DecimalField(max_digits=10, decimal_places=2)
    total_meters = models.DecimalField(max_digits=10, decimal_places=2)
    taxes = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    size = models.CharField(max_length=50, blank=True)
    color = models.CharField(max_length=50, blank=True)
    is_printed = models.BooleanField(default=False)
    stock_quantity = models.PositiveIntegerField(default=0)
    supplier = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='inventory/', blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.item_name} ({self.item_type})"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.SET_NULL, null=True, blank=True)
    product_type = models.CharField(max_length=20, choices=InventoryItem.ITEM_TYPE_CHOICES)
    measurements = models.JSONField(blank=True, null=True, help_text="Store measurements as JSON")
    status = models.CharField(max_length=50, default='Pending')
    notes = models.TextField(blank=True)
    order_date = models.DateField(auto_now_add=True)
    delivery_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='orders/', blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"Order #{self.id} for {self.customer.name}"

class Requirement(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='requirements', null=True, blank=True)
    description = models.TextField()
    is_fulfilled = models.BooleanField(default=False)
    steps_done = models.JSONField(blank=True, null=True, help_text="Checklist of steps done")
    steps_not_done = models.JSONField(blank=True, null=True, help_text="Checklist of steps not done")
    attachment = models.FileField(upload_to='requirements/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"Requirement for Order #{self.order.id if self.order else 'N/A'}"

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Pending')
    payment_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"Payment for Order #{self.order.id} - {self.amount}"

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()
    def __str__(self):
        return self.name

class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='purchases')
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='purchases')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)
    history = HistoricalRecords()
    def __str__(self):
        return f"Purchase of {self.quantity} {self.item} from {self.supplier}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    url = models.CharField(max_length=255, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Notification for {self.user.username}: {self.message[:30]}"

class CustomerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer = models.OneToOneField('Customer', on_delete=models.CASCADE)
    def __str__(self):
        return f"CustomerUser: {self.user.username}"
