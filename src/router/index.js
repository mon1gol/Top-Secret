import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/:category_slug/:tournament_slug',
      name: 'tournament',
      component: () => import('../views/TournamentView.vue'),
    },
    {
      path: '/sign-up',
      name: 'signUp',
      component: () => import('../views/SignUpView.vue'),
    },
    {
      path: '/log-in',
      name: 'login',
      component: () => import('../views/LoginView.vue'),
    },

  ],
})

export default router
