from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ['clientId', 'created_at', 'updated_at']
        extra_kwargs = {
            'fullName': {'help_text': 'Nom complet du client.'},
            'phone': {'help_text': 'Téléphone du client.'},
            'email': {'help_text': 'Adresse email du client (unique).'},
            'cniNumber': {'help_text': 'Numéro de CNI du client (unique).'},
            'state': {'help_text': 'État du client (active ou inactive).'},
        }