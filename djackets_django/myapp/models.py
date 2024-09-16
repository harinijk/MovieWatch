from django.db import models

class LikedMovie(models.Model):
    movie_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    poster_url = models.URLField()

    def __str__(self):
        return self.title
    
class Review(models.Model):
    movie_id = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text