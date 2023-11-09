"""
Views for the recipe APIs
"""
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination


from core.models import Breed, Dog, Answer
from recipe import serializers



class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 100


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'name',
                OpenApiTypes.STR,
        
            ),
            OpenApiParameter(
                'offset',
                OpenApiTypes.INT,
                description='The initial index from which to return the result.',
            ),
            OpenApiParameter(
                'limit',
                OpenApiTypes.INT,
                description='Number of results to return per page.',
            ),
        ]
    )
    
)
class BreedsViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = serializers.BreedSerializer
    queryset = Breed.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):

        name = self.request.query_params.get('name')
        offset = self.request.query_params.get('offset')
        queryset = self.queryset
        if name:
            queryset = queryset.filter(name=name)
        if offset:
            queryset = queryset.filter(id__gte=offset)
        return queryset.filter(
            user=self.request.user
        ).order_by('-id').distinct()

   

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)

    
@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'name',
                OpenApiTypes.STR,
        
            ),
            OpenApiParameter(
                'breed',
                OpenApiTypes.STR,
        
            ),
            OpenApiParameter(
                'breed__name',
                OpenApiTypes.STR,
        
            ),
            OpenApiParameter(
                'page',
                OpenApiTypes.INT,
                description='A page number within the paginated result set',
            ),
        ]
    )
    
)
class DogsViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = serializers.DogSerializer
    queryset = Dog.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):

        name = self.request.query_params.get('name')
        breed = self.request.query_params.get('breed')
        breed__name = self.request.query_params.get('breed__name')
        queryset = self.queryset
        if name:
            queryset = queryset.filter(name=name)
        if breed:
            queryset = queryset.filter(breed__name=breed)
        elif breed__name:
            queryset = queryset.filter(breed__name=breed__name)

        return queryset.filter(
            user=self.request.user
        ).order_by('-id').distinct()


    def perform_create(self, serializer):

        serializer.save(user=self.request.user)
      
      
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class AnswerView(CreateAPIView):
    
    serializer_class = serializers.AnswerSerializer
    queryset = Answer.objects.all()

    def perform_create(self, serializer):
        # Puedes realizar acciones adicionales antes de guardar la instancia
        serializer.save()

