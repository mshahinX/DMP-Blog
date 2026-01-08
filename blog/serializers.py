from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'created_at']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

        extra_kwargs = {
            'password': {'write_only': True}    
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
