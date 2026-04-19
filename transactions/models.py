from django.db import models
from accounts.models import Account

class Transaction(models.Model):
    transactionId = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transactionType = models.SlugField(choices=[('depot', 'Depot'), ('retrait', 'Retrait')], default='depot')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    balanceBefore = models.DecimalField(max_digits=10, decimal_places=2)
    balanceAfter = models.DecimalField(max_digits=10, decimal_places=2)
    dateTime = models.DateTimeField(auto_now_add=True)
    state = models.SlugField(choices=[('success', 'Success'), ('failed', 'Failed')], default='success')

    def __str__(self):
        return f"{self.account.accountNumber} - {self.amount}"
