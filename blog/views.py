from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer, RegisterSerializer, LogoutSerializer
from django.shortcuts import get_object_or_404
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample

class RegisterView(APIView):
    permission_classes = []

    @extend_schema(
        request=RegisterSerializer,
        examples=[
            OpenApiExample(
                name="Example",
                value={
                    "username": "newuser",
                    "password": "newpassword123"
                }
            )
        ],
        responses={201: OpenApiResponse(description="User registered successfully.")}
    )    

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            {'message': 'User registered successfully.'}, 
            status=status.HTTP_201_CREATED
        )

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=LogoutSerializer,
        responses={205: OpenApiResponse(description="User logged out successfully.")}
    )

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            token = RefreshToken(serializer.validated_data['refresh'])
            token.blacklist()
            return Response({'message': 'User logged out successfully.'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'error': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)

class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Blog.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)