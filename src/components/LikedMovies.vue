<template>
    <div class="liked-movies">
      <h1>Liked Movies</h1>
      <div class="movies-list">
        <div class="movie" v-for="movie in likedMovies" :key="movie.movie_id">
          <router-link :to="'/movie/'+movie.movie_id" class="movie-link">
            <div class="product-image">
              <img :src="movie.poster_url" alt="Movie Poster" />
            </div>
            <div class="detail">
              <h3>{{ movie.title }}</h3>
             
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  
  export default {
    setup() {
      const likedMovies = ref([]);
  
      const fetchLikedMovies = async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/v1/likes/');
    likedMovies.value = response.data;
    console.log('Fetched liked movies:', likedMovies.value); 
  } catch (error) {
    console.error('Error fetching liked movies:', error);
  }
};
  
      onMounted(fetchLikedMovies);
  
      return {
        likedMovies
      };
    }
  };
  </script>
  
  <style lang="scss">
  .liked-movies {
    padding: 16px;
  
    .movies-list {
      display: flex;
      flex-wrap: wrap;
  
      .movie {
        flex: 1 1 30%;
        margin: 8px;
        .movie-link {
          display: flex;
          flex-direction: column;
          height: 100%;
  
          .product-image img {
            width: 100%;
            height: 200px;
            object-fit: cover;
          }
  
          .detail {
            background-color: #4965a3;
            padding: 16px;
            border-radius: 8px;
  
            .year {
              color: white;
              font-size: 14px;
            }
  
            h3 {
              color: white;
              font-size: 18px;
            }
          }
        }
      }
    }
  }
  </style>
  