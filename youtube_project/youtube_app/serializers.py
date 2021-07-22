from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment

        # fields = ['id', 'videoId', 'userComment', 'like', 'dislike', 'originalComment']
        fields = '__all__'

