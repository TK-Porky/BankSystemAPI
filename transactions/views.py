from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter, OpenApiTypes
from .models import Transaction
from .serializers import TransactionSerializer

@extend_schema(
    tags=['Transactions'],
    request=TransactionSerializer,
    responses=TransactionSerializer,
    description='Créer une nouvelle transaction de dépôt ou de retrait.',
    examples=[
        OpenApiExample(
            'CreateTransactionRequest',
            value={
                'account': 1,
                'transactionType': 'depot',
                'amount': '250.00',
                'balanceBefore': '1000.00',
                'balanceAfter': '1250.00',
                'state': 'success',
            },
            request_only=True,
            summary='Exemple de payload pour créer une transaction',
        ),
        OpenApiExample(
            'CreateTransactionResponse',
            value={
                'transactionId': 1,
                'account': 1,
                'transactionType': 'depot',
                'amount': '250.00',
                'balanceBefore': '1000.00',
                'balanceAfter': '1250.00',
                'dateTime': '2026-04-19T15:00:00Z',
                'state': 'success',
            },
            response_only=True,
            summary='Réponse renvoyée après création de la transaction',
        ),
    ],
)
@api_view(['POST'])
def create_transaction(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=['Transactions'],
    responses=TransactionSerializer,
    parameters=[
        OpenApiParameter('transaction_id', OpenApiTypes.INT, OpenApiParameter.PATH, description='Identifiant de la transaction'),
    ],
    description='Récupère une transaction par son identifiant.',
)
@api_view(['GET'])
def get_transaction(request, transaction_id):
    try:
        transaction = Transaction.objects.get(pk=transaction_id)
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TransactionSerializer(transaction)
    return Response(serializer.data)

@extend_schema(
    tags=['Transactions'],
    responses=TransactionSerializer(many=True),
    description='Liste toutes les transactions.',
)
@api_view(['GET'])
def get_transactions(request):
    transactions = Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)
