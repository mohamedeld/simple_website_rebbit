from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source = 'poster.username')
    poster_id = serializers.ReadOnlyField(source = 'poster.id')
    
    class Meta:
        model = Post
        fields = '__all__'