from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        read_only_fields = ['accountId', 'opened_at', 'updated_at']
        extra_kwargs = {
            'accountNumber': {'help_text': 'Numéro de compte unique.'},
            'client': {'help_text': 'Identifiant du client propriétaire du compte.'},
            'balance': {'help_text': 'Solde actuel du compte.'},
            'accountType': {'help_text': 'Type de compte : epargne ou courant.'},
        }