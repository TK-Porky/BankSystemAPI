from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter, OpenApiTypes
from .models import Client
from .serializers import ClientSerializer

@extend_schema(
    tags=['Clients'],
    request=ClientSerializer,
    responses=ClientSerializer,
    description='Créer un nouveau client avec toutes les informations obligatoires.',
    examples=[
        OpenApiExample(
            'CreateClientRequest',
            value={
                'fullName': 'Theophile Kevin',
                'phone': '+237123456789',
                'email': 'theophile.kevin@example.com',
                'cniNumber': 'CNI1234567',
                'state': 'active',
            },
            request_only=True,
            summary='Exemple de payload pour créer un client',
        ),
        OpenApiExample(
            'CreateClientResponse',
            value={
                'clientId': 1,
                'fullName': 'Theophile Kevin',
                'phone': '+237123456789',
                'email': 'theophile.kevin@example.com',
                'cniNumber': 'CNI1234567',
                'state': 'active',
                'created_at': '2026-04-19T15:00:00Z',
                'updated_at': '2026-04-19T15:00:00Z',
            },
            response_only=True,
            summary='Réponse renvoyée après création du client',
        ),
    ],
)
@api_view(['POST'])
def create_client(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=['Clients'],
    responses=ClientSerializer,
    parameters=[
        OpenApiParameter('client_id', OpenApiTypes.INT, OpenApiParameter.PATH, description='Identifiant du client'),
    ],
    description='Récupère un client par son identifiant.',
)
@api_view(['GET'])
def get_client(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ClientSerializer(client)
    return Response(serializer.data)

@extend_schema(
    tags=['Clients'],
    responses=ClientSerializer(many=True),
    description='Liste tous les clients existants.',
)
@api_view(['GET'])
def get_clients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)
