from django.db import models
from accounts.models import UserBankAccount
from .constants import TRANSACTION_TYPE

# Create your models here.
class Transaction(models.Model):
    account = models.ForeignKey(UserBankAccount, related_name='transations', on_delete=models.CASCADE) # ekjon user er multiple transactions hote pare

    amount = models.DecimalField(decimal_places=2, max_digits = 12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits = 12)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False) 
    
    class Meta:
        ordering = ['timestamp'] 

class Bankrupt(models.Model):
    is_bankrupt = models.BooleanField(default=False)

    def __str__(self):
        return f"Bankrupt: {self.is_bankrupt}"