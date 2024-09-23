from django.db import models

class Transaction(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),
    ]
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField()
    description = models.TextField()

class Budget(models.Model):
    category = models.CharField(max_length=20)
    limit = models.DecimalField(max_digits=10, decimal_places=2)

class FinancialGoal(models.Model):
    goal_name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
