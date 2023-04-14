from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Relationship, UserImageSelection, Post, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_staff', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'default': False},
            'is_superuser': {'default': False},
        }
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_staff=validated_data.get('is_staff', False),
            is_superuser=validated_data.get('is_superuser', False),
        )
        return User
        
class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'avatar', 'highlight_reel', 'relationships')

class UserImageSelectionSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(read_only=True)
    
    class Meta:
        model = UserImageSelection
        fields = ('id', 'user', 'user_profile', 'image')

class RelationshipSerializer(serializers.ModelSerializer):

    user_profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = Relationship
        fields = ('id', 'user_profile', 'from_user', 'to_user', 'relationship_type')

class CommentSerializer(serializers.ModelSerializer):

    user_profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id','user', 'user_profile', 'post', 'content', 'created_at')

class PostSerializer(serializers.ModelSerializer):

    user_profile = UserProfileSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'user', 'user_profile', 'content', 'image', 'created_at', 'comments')