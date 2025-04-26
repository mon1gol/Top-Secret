<script setup>
import { RouterLink, RouterView } from 'vue-router'
// import { Icon } from "@iconify/vue";
</script>

<template>
  <header class="bg-blue-four">
    <div class="flex justify-center">
      <nav class="container mx-auto px-4 fixed flex h-15 items-center justify-between gap-5 py-5 font-medium text-gray-900 z-10">
        <div class="space-x-5">
          <RouterLink class="category-btn-hover-white" to="/">Главная</RouterLink>
          <RouterLink class="category-btn-hover-white" to="/about">О сайте</RouterLink>
          <RouterLink class="category-btn-hover-white" v-if="userStatus" to="/attach-project">Прикрепить проект</RouterLink>
          <RouterLink class="category-btn-hover-white" v-if="userStatus" to="/my-tournaments">Мои соревнования</RouterLink>
        </div>
        <div class="space-x-5">
          <RouterLink class="category-btn-hover-white" v-if="!userStatus" to="/sign-up">Регистрация</RouterLink>
          <RouterLink class="category-btn-hover-white" v-if="!userStatus" to="/log-in">Войти</RouterLink>
          <div v-if="userStatus" class="relative inline-block">
            <div class="cursor-pointer">Результаты</div>
            <div class="dropdown-menu absolute hidden bg-white text-black py-2 px-4 rounded shadow-lg">
                <RouterLink to="/my-results">Мои результаты</RouterLink>
                <RouterLink to="/">Лучшие команды</RouterLink>
            </div>
          </div>
          <RouterLink class="category-btn-hover-white" v-if="userStatus" to="/my-account">Профиль</RouterLink>
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
