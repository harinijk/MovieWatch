<template>
  <div class="home">
    <div class="feature-card">
      <router-link to="/movie/tt0409591">
        <img src="https://m.media-amazon.com/images/I/81ai6zx6eXL._AC_SL1304_.jpg" 
          alt="Avengers Poster" class="featured-img">
        <div class="detail">
          <h3>Avengers</h3>
          <p>Nick Fury assembles Iron Man, Captain America, Thor, the Hulk, Black Widow, 
            and Hawkeye to stop Loki from threatening global security. Their teamwork is crucial to preventing a world-threatening catastrophe.</p>
        </div>
      </router-link>
    </div>
    <form @submit.prevent="SearchMovies" class="search-box">
      <input type="text" placeholder="What are you looking for?" v-model="search"/>
      <input type="submit" value="Search"/> 
    </form>
    <div class="movies-list">
      <div class="movie" v-for="movie in movies" :key="movie.imdbID">
        <div class="movie-link">
          <router-link :to="'/movie/'+movie.imdbID">
            <div class="product-image">
              <img :src="movie.Poster" alt="Movie Poster" />
              <div class="type">{{ movie.Type }}</div>
            </div>
          </router-link>
          <div class="detail">
            <p class="year">{{ movie.Year }}</p>
            <h3>{{ movie.Title }}</h3>
            <div class="like" @click.stop="likeMovie(movie)">
              <svg class="heart-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" :class="{ liked: isLiked(movie) }">
                <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41 0.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';
import env from '@/env.js';

export default {
  setup() {
    const movies = ref([]);
    const search = ref('');
    const likedMovies = ref([]);

    const SearchMovies = async () => {
      try {
        const response = await axios.get(`http://www.omdbapi.com/?apikey=${env.apikey}&s=${search.value}`);
        movies.value = response.data.Search;
      } catch (error) {
        console.error('Error searching movies:', error);
      }
    };

    const likeMovie = async (movie) => {
      console.log('Movie ID:', movie.imdbID);
      console.log('Is liked:', isLiked(movie));
      try {
        if (isLiked(movie)) {
          const response = await axios.delete(`http://localhost:8000/api/v1/unlike/${movie.imdbID}/`);
          if (response.status === 204) { 
            likedMovies.value = likedMovies.value.filter(id => id !== movie.imdbID);
          }
        } else {
          const response = await axios.post('http://localhost:8000/api/v1/likes/', {
            movie_id: movie.imdbID,
            title: movie.Title,
            poster_url: movie.Poster,
          });
          if (response.status === 201) {
            likedMovies.value.push(movie.imdbID);
          }
        }
      } catch (error) {
        console.error('Error liking or unliking movie:', error);
      }
    };

    const isLiked = (movie) => {
    //  console.log('Checking if liked:', movie.imdbID);
     // console.log('Current likedMovies array:', likedMovies.value);
      return likedMovies.value.includes(movie.imdbID);
    };

    return {
      movies,
      search,
      SearchMovies,
      likeMovie,
      isLiked,
    };
  },
};
</script>

<style lang="scss">
.home {
  .feature-card {
    position: relative;

    .featured-img {
      display: block;
      width: 100%;
      height: 300px;
      object-fit: cover;
      position: relative;
      z-index: 0;
    }

    .detail {
      position: absolute;
      left: 0;
      right: 0;
      bottom: 0;
      background-color: rgba(0, 0, 0, 0.6);
      padding: 16px;
      z-index: 1;

      h3 {
        color: white;
        margin-bottom: 16px;
      }

      p {
        color: white;
      }
    }
  }

  .search-box {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 16px;

    input {
      display: block;
      appearance: none;
      border: none;
      outline: none;
      background: none;

      &[type="text"] {
        width: 100%;
        color: white;
        background-color: #22303e;
        font-size: 20px;
        padding: 10px 16px;
        border-radius: 8px;
        margin-bottom: 15px;
        transition: 0.4s;

        &::placeholder {
          color: #f3f3f3;
        }

        &:focus {
          box-shadow: 0px 3px 6px rgb(0, 0, 0, 0.2);
        }
      }

      &[type="submit"] {
        width: 100%;
        max-width: 300px;
        background-color: rgb(115, 192, 132);
        padding: 16px;
        border-radius: 8px;
        color: white;
        font-size: 20px;
        text-transform: uppercase;
        transition: 0.4s;

        &:active {
          background-color: rgb(54, 156, 54);
        }
      }
    }
  }

  .movies-list {
    display: flex;
    flex-wrap: wrap;
    margin: 0px 8px;

    .movie {
      max-width: 50%;
      flex: 1 1 50%;
      padding: 16px 8px;

      .movie-link {
        display: flex;
        flex-direction: column;
        height: 100%;

        .product-image {
          position: relative;
          display: block;

          img {
            display: block;
            width: 100%;
            height: 275px;
            object-fit: center;
          }

          .type {
            position: absolute;
            padding: 8px 16px;
            background-color: #42B883;
            color: white;
            bottom: 16px;
            left: 0px;
            text-transform: capitalize;
          }
        }
        
        .detail {
          background-color: #4965a3;
          padding: 16px 8px;
          flex: 1 1 100%;
          border-radius: 0px 0px 8px 8px;

          .year {
            color: white;
            font-size: 14px;
          }

          h3 {
            color: white;
            font-weight: 600;
            font-size: 18px;
          }

          .like {
            cursor: pointer;
            .heart-icon {
              fill: none;
              stroke: black;
              stroke-width: 2px;
              width: 24px;
              height: 24px;
              &.liked {
                fill: red;
              }
            }
          }
        }
      }
    }
  }
}
</style>


