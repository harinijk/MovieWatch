from rest_framework import serializers
from .models import LikedMovie
from .models import Review


class LikedMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedMovie
        fields = ['movie_id', 'title', 'poster_url']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'