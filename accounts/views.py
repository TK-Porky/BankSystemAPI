from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter, OpenApiTypes
from .models import Account
from .serializers import AccountSerializer

@extend_schema(
    tags=['Accounts'],
    request=AccountSerializer,
    responses=AccountSerializer,
    description='Créer un compte bancaire lié à un client existant.',
    examples=[
        OpenApiExample(
            'CreateAccountRequest',
            value={
                'accountNumber': 'FR7612345678901234567890123',
                'client': 1,
                'balance': '1000.00',
                'accountType': 'courant',
            },
            request_only=True,
            summary='Exemple de payload pour créér un compte',
        ),
        OpenApiExample(
            'CreateAccountResponse',
            value={
                'accountId': 1,
                'accountNumber': 'FR7612345678901234567890123',
                'client': 1,
                'balance': '1000.00',
                'accountType': 'courant',
                'opened_at': '2026-04-19T15:00:00Z',
                'updated_at': '2026-04-19T15:00:00Z',
            },
            response_only=True,
            summary='Réponse renvoyée après création du compte',
        ),
    ],
)
@api_view(['POST'])
def create_account(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=['Accounts'],
    responses=AccountSerializer,
    parameters=[
        OpenApiParameter('account_id', OpenApiTypes.INT, OpenApiParameter.PATH, description='Identifiant du compte'),
    ],
    description='Récupère un compte par son identifiant.',
)
@api_view(['GET'])
def get_account(request, account_id):
    try:
        account = Account.objects.get(pk=account_id)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AccountSerializer(account)
    return Response(serializer.data)

@extend_schema(
    tags=['Accounts'],
    responses=AccountSerializer(many=True),
    description='Liste tous les comptes.',
)
@api_view(['GET'])
def get_accounts(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)
