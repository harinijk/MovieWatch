from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import LikedMovie
from .serializers import LikedMovieSerializer
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Review
from rest_framework import generics
from .serializers import ReviewSerializer
import logging

logger = logging.getLogger(__name__)


@api_view(['POST', 'DELETE'])
def like_movie(request, movie_id=None):
    print(f"Request method: {request.method}")
    print(f"Movie ID: {movie_id}")

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            movie_id = data.get('movie_id')
            title = data.get('title')
            poster_url = data.get('poster_url')

            if not movie_id:
                return JsonResponse({'status': 'error', 'message': 'movie_id is required'}, status=400)
            
            if not title or not poster_url:
                return JsonResponse({'status': 'error', 'message': 'title and poster_url are required'}, status=400)

            liked_movie, created = LikedMovie.objects.get_or_create(
                movie_id=movie_id,
                defaults={'title': title, 'poster_url': poster_url}
            )
            if not created:
                return JsonResponse({'status': 'already liked'})
            return JsonResponse({'status': 'liked'})
        except Exception as e:
            logger.error(f"Error processing POST request: {e}")
            return JsonResponse({'status': 'error', 'message': 'Error processing request'}, status=500)
    
    elif request.method == 'DELETE':
        if not movie_id:
            return JsonResponse({'status': 'error', 'message': 'movie_id is required'}, status=400)

        try:
            liked_movie = LikedMovie.objects.get(movie_id=movie_id)
            liked_movie.delete()
            return JsonResponse({'status': 'unliked'})
        except LikedMovie.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Movie not found'}, status=404)
        except Exception as e:
            logger.error(f"Error processing DELETE request: {e}")
            return JsonResponse({'status': 'error', 'message': 'Error processing request'}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)


class LikedMovieViewSet(viewsets.ModelViewSet):
    queryset = LikedMovie.objects.all()
    serializer_class = LikedMovieSerializer

class LikedMovieListView(APIView):
    def get(self, request):
        liked_movies = LikedMovie.objects.all()
        serializer = LikedMovieSerializer(liked_movies, many=True)
        return Response(serializer.data)


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie_id = self.request.query_params.get('movie_id')
        if movie_id:
            return Review.objects.filter(movie_id=movie_id)
        return Review.objects.all()

    def perform_create(self, serializer):
        serializer.save()