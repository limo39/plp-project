from django.db import models

# Model for tracking Expenses
class Expense(models.Model):
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.category} - {self.amount} on {self.date}"

# Model for setting Budgets
class Budget(models.Model):
    category = models.CharField(max_length=100)
    limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Budget for {self.category} - {self.limit}"

# Model for Financial Goals
class FinancialGoal(models.Model):
    goal_name = models.CharField(max_length=200)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Goal: {self.goal_name}, Target: {self.target_amount}"
