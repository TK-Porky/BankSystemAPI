from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['transactionId', 'dateTime']
        extra_kwargs = {
            'account': {'help_text': 'Identifiant du compte concerné par la transaction.'},
            'transactionType': {'help_text': 'Type de transaction : depot ou retrait.'},
            'amount': {'help_text': 'Montant de la transaction.'},
            'balanceBefore': {'help_text': 'Solde avant la transaction.'},
            'balanceAfter': {'help_text': 'Solde après la transaction.'},
            'state': {'help_text': 'État de la transaction (success ou failed).'},
        }