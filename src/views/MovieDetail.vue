<template>
  <div class="movie-detail" v-if="movie">
    <h2>{{ movie.Title }}</h2>
    <p>{{ movie.Year }}</p>
    <img :src="movie.Poster" alt="Movie Poster" class="featured-img" />
    <p>{{ movie.Plot }}</p>

    <button @click="showReviewForm = true" class="add-review-btn">
      <i class="fas fa-plus"></i> Add Review
    </button>

    <div v-if="showReviewForm" class="review-form-overlay">
      <div class="review-form">
        <h3>Write a Review</h3>
        <textarea v-model="reviewText" placeholder="Write your review here..."></textarea>
        <button @click="submitReview">Submit</button>
        <button @click="showReviewForm = false">Cancel</button>
      </div>
    </div>

    <div class="reviews">
      <h3>Reviews</h3>
      <div v-for="review in reviews" :key="review.id" class="review">
        <p>{{ review.text }}</p>
      </div>
    </div>
  </div>
</template>


<script>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import env from '@/env.js';

export default {
  setup() {
    const route = useRoute();
    const movie = ref(null);
    const reviews = ref([]);
    const showReviewForm = ref(false);
    const reviewText = ref('');

    const fetchMovieDetails = async () => {
      const movieId = route.params.id;
      try {
        const response = await axios.get(`http://www.omdbapi.com/?apikey=${env.apikey}&i=${movieId}`);
        if (response.data.Response === 'True') {
          movie.value = response.data;
          fetchReviews(movieId); // Fetch reviews after getting movie details
        } else {
          console.error('Error fetching movie details:', response.data.Error);
        }
      } catch (error) {
        console.error('Error fetching movie details:', error);
      }
    };

    const fetchReviews = async (movieId) => {
      try {
        const response = await axios.get(`http://localhost:8000/api/v1/reviews/${movieId}`);
        reviews.value = response.data;
      } catch (error) {
        console.error('Error fetching reviews:', error);
      }
    };

    const submitReview = async () => {
      const movieId = route.params.id;
      try {
        const response = await axios.post(`http://localhost:8000/api/v1/postreviews/`, {
          movie_id: movieId,
          text: reviewText.value,
        });
        if (response.status === 201) {
          reviews.value.push(response.data);
          reviewText.value = '';
          showReviewForm.value = false;
        }
      } catch (error) {
        console.error('Error submitting review:', error);
      }
    };

    onMounted(fetchMovieDetails);

    return {
      movie,
      reviews,
      showReviewForm,
      reviewText,
      submitReview,
    };
  },
};

</script>

<style lang="scss">
.movie-detail {
  padding: 16px;

  h2 {
    color: white;
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 16px;
  }

  .featured-img {
    display: block;
    max-width: 200px;
    margin-bottom: 16px;
  }

  p {
    color: white;
    font-size: 18px;
    line-height: 1.4;
  }

  .add-review-btn {
    background: none;
    border: none;
    font-size: 24px;
    cursor: pointer;
    margin-top: 20px;
    color: white;
  }

  .review-form-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.7);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .review-form {
    background: white;
    padding: 20px;
    border-radius: 8px;
    text-align: center;

    h3 {
      margin-bottom: 10px;
    }

    textarea {
      width: 100%;
      height: 100px;
      margin-bottom: 10px;
    }

    button {
      margin: 5px;
    }
  }

  .reviews {
    margin-top: 20px;

    .review {
      background: white;
      padding: 10px;
      margin-bottom: 10px;
      border-radius: 8px;
      
      p{
        color:black;
      }
    }
  }
}
</style>
