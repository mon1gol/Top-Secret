<script setup>
import { RouterLink, RouterView } from 'vue-router'
// import { Icon } from "@iconify/vue";
</script>

<template>
  <header>
    <div class="wrapper">
      <nav class="bg-blue-four fixed flex h-15 w-lvw items-center gap-5 px-10 py-5 font-bold text-gray-700">
        <RouterLink to="/">Главная</RouterLink>
        <RouterLink to="/about">О сайте</RouterLink>
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
    return {

    }
  },
  beforeCreate() {
    const commonStore = useCommonStore()
    commonStore.initializeStore()

    const token = commonStore.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {

  },
}
</script>

<style scoped>

</style>
