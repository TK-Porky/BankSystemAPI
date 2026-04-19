from django.db import models
from clients.models import Client

class Account(models.Model):
    accountId = models.AutoField(primary_key=True)
    accountNumber = models.CharField(max_length=34, unique=True, help_text='Numéro de compte unique')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    accountType = models.SlugField(choices=[('epargne', 'Epargne'), ('courant', 'Courant')], default='epargne')
    opened_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.accountNumber
