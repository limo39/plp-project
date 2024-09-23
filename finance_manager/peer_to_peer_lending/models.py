from django.db import models

class Borrower(models.Model):
    name = models.CharField(max_length=100)
    verification_status = models.BooleanField(default=False)

class Loan(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    repayment_period = models.IntegerField()  # in months

class Investor(models.Model):
    name = models.CharField(max_length=100)
    portfolio_value = models.DecimalField(max_digits=10, decimal_places=2)
