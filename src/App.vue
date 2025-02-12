<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import { Icon } from "@iconify/vue";
</script>

<template>
  <header>
    <div class="wrapper">
      <!-- <HelloWorld msg="You did it!" /> -->
      
      <nav class="bg-blue-four h-15 p-5 flex items-center gap-5 font-bold text-gray-700">
        <RouterLink to="/">Главная</RouterLink>
        <RouterLink to="/about">О сайте</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>

</style>
