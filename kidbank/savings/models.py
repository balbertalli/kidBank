import uuid
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    
    @property
    def balance(self):
        deposits = self.transaction_set.filter(type=1).aggregate(models.Sum('amount', default=0))
        withdrawals = self.transaction_set.filter(type=0).aggregate(models.Sum('amount', default=0))
        balance = deposits['amount__sum'] - withdrawals['amount__sum']
        return balance
    
    def __str__(self):
        return self.owner.username
        

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        (0, 'Withdrawal'),
        (1, 'Deposit'),
    ]
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.IntegerField(choices=TRANSACTION_TYPE_CHOICES)
    memo = models.TextField(blank=True)
        
    def __str__(self):
        return f'{self.account.owner.username} / {self.timestamp.date()} / ${self.amount}'
        
    class Meta:
        ordering = ['-timestamp']
        
        
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'memo']
        
        
        