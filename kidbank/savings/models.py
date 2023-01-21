from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField()
    
    @property
    def balance(this):
        deposits = this.deposit_set.aggregate(models.Sum('amount'))
        withdrawals = this.withdrawal_set.aggregate(models.Sum('amount'))
        return deposits['amount__sum'] - withdrawals['amount__sum']
        

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    memo = models.TextField()
    
    class Meta:
        abstract = True
        
class Deposit(Transaction):
    pass

class Withdrawal(Transaction):
    pass
