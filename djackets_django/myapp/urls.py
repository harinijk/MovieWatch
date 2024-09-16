from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LikedMovieViewSet, like_movie, LikedMovieListView
from .views import ReviewListCreateView

router = DefaultRouter()
router.register(r'likes', LikedMovieViewSet, basename='like')

urlpatterns = [
    path('api/v1/', include(router.urls)), 
    path('api/v1/likes/', like_movie, name='like_movie'),  # POST endpoint to like a movie
    path('api/v1/unlike/<str:movie_id>/', like_movie, name='unlike_movie'), # DELETE endpoint to unlike a movie
    path('api/v1/reviews/<str:movie_id>/', ReviewListCreateView.as_view(), name='review-list-create'), # GET endpoint to get reviews
    path('api/v1/postreviews/', ReviewListCreateView.as_view(), name='review-list-create'),   # POST endpoint to post reviews
]
