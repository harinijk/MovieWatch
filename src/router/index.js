import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue';
import MovieDetail from '@/views/MovieDetail.vue';
import LikedMovies from '@/components//LikedMovies';


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/movie/:id',
    name: 'MovieDetail',
    component: MovieDetail,
    props: true,
  },
  { path: '/liked-movies', component: LikedMovies },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

