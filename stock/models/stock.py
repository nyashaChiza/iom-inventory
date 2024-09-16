from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Department(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Stock(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  # Link to department
    quantity = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.department.name})"  # Display department with stock


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='source_department')  # Source department
    destination = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='destination_department')  # Destination department
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.approved}"


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('ADD', 'Addition'),
        ('REMOVE', 'Removal')
    ]

    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='transactions')
    quantity = models.IntegerField()
    transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPE_CHOICES)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.stock.name} - {self.transaction_type}"
