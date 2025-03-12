import { createRouter, createWebHistory } from 'vue-router'
import { useCommonStore } from '@/stores'
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
      path: '/:category_slug/:tournament_slug/submit',
      name: 'submitTournament',
      component: () => import('../views/SubmitTournamentView.vue'),
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
    {
      path: '/my-account',
      name: 'myAccount',
      component: () => import('../views/MyAccountView.vue'),
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/my-tournaments',
      name: 'myTournaments',
      component: () => import('../views/MyTournamentsView.vue'),
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/attach-project',
      name: 'attachProject',
      component: () => import('../views/AttachProjectView.vue'),
      meta: {
        requireLogin: true
      }
    },

  ],
})

router.beforeEach((to, from, next) => {
  const commonStore = useCommonStore()

  if(to.matched.some(record => record.meta.requireLogin) && !commonStore.isAuthenticated){
    next({
      name: 'login',
      query: { to: to.path }
    });
  } else {
    next()
  }
})

export default router
