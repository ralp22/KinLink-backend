from rest_framework import serializers
from .models import User, Relationship, UserImageSelection, Post, Comment

class UserImageSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImageSelection
        fields = ('id', 'user', 'image')

class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = ('id', 'from_user', 'to_user', 'relationship_type')
class UserProfileSerializer(serializers.ModelSerializer):
    highlight_reel = UserImageSelectionSerializer(many=True, read_only=True)
    relationships = RelationshipSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'user', 'avatar', 'highlight_reel', 'relationships')

class CommentSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id','user', 'post', 'content', 'created_at')

class PostSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'user', 'content', 'image', 'created_at', 'comments')