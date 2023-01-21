from django.contrib import admin
from .models import Account, Deposit, Withdrawal

admin.site.register(Account)
admin.site.register(Deposit)
admin.site.register(Withdrawal)
