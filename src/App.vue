<script setup>
import { RouterLink, RouterView } from 'vue-router'
// import { Icon } from "@iconify/vue";
</script>

<template>
  <header>
    <div>
      <nav class="bg-blue-four fixed flex h-15 w-lvw items-center justify-between gap-5 px-20 py-5 font-bold text-gray-900">
        <div class="space-x-5 font-normal">
          <RouterLink to="/">Главная</RouterLink>
          <RouterLink to="/about">О сайте</RouterLink>
        </div>
        <div class="space-x-5 font-normal">
          <RouterLink v-if="!userStatus" to="/log-in">Войти</RouterLink>
          <RouterLink v-if="!userStatus" to="/sign-up">Регистрация</RouterLink>
          <RouterLink v-if="userStatus" to="/attach-project">Прикрепить проект</RouterLink>
          <RouterLink v-if="userStatus" to="/my-tournaments">Мои соревнования</RouterLink>
          <RouterLink v-if="userStatus" to="/my-account">Профиль</RouterLink>
        </div>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<script>
import { useCommonStore } from './stores';
import axios from 'axios';


export default {
  data() {
    return {}
  },
  computed: {
    userStatus() {
      const commonStore = useCommonStore();
      return commonStore.isAuthenticated;
    },
  },
  created() {
    const commonStore = useCommonStore()
    commonStore.initializeStore()

    const token = commonStore.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
}
</script>
