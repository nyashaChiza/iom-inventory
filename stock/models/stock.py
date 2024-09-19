from django.db import models
from django.conf import settings

STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    ]
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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    source = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='source_department')  # Source department
    destination = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='destination_department')  # Destination department
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        status = 'Approved' if self.approved else 'Not Approved'
        return f"{self.user} - {status}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.approved:
            self.update_stock_balances()
        
    def update_stock_balances(self):
        for transaction in self.transactions.all():
            if transaction.transaction_type == 'ADD':
                transaction.stock.quantity += transaction.quantity
            elif transaction.transaction_type == 'REMOVE':
                transaction.stock.quantity -= transaction.quantity
            
            # Save the updated stock quantity
            transaction.stock.save()


class Approval(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='approvals')
    approver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Approval for {self.request} by {self.approver} - Status: {self.status}"

    def save(self, *args, **kwargs):
        # Call the parent save method
        super().save(*args, **kwargs)
        
        # Check if all approvals for the request are approved
        all_approved = all(approval.status == 'Approved' for approval in self.request.approvals.all())
        # Update the request's approved status
        self.request.approved = all_approved
        self.request.save()

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
