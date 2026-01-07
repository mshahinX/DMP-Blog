from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer
from django.shortcuts import get_object_or_404
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password') 

        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        User.objects.create_user(
            username=username, 
            password=password)
        
        return Response(
            {'message': 'User registered successfully.'}, 
            status=status.HTTP_201_CREATED
        )

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out."}, status=200)
       
        except Exception as e:
            return Response({"error": "Invalid token."}, status=400)  


class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Blog.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)