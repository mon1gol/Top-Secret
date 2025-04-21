<template>
  <div class="gradient-blue flex flex-col h-lvh w-lvw items-center justify-center">
    <h1 class="text-6xl font-bold text-center">Профиль</h1>
    <div class="h-120 w-100 px-10 py-15 rounded-xl">
      <form @submit.prevent="submitForm" class="flex flex-col gap-5">
        <div>
          <label for="username" class="block text-sm/6 font-semibold text-black">Логин</label>
          <div class="mt-2">
            <input v-model="username" type="text"
              class="block w-full rounded-xl bg-white px-3.5 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 placeholder:text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 transition-all duration-150">
          </div>
        </div>
        <div>
          <label for="password" class="block text-sm/6 font-semibold text-black">Новый пароль</label>
          <div class="mt-2">
            <input v-model="password" type="password"
              class="block w-full rounded-xl bg-white px-3.5 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 placeholder:text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 transition-all duration-150">
          </div>
        </div>
        <div>
          <label for="password2" class="block text-sm/6 font-semibold text-black">Повторите новый пароль</label>
          <div class="mt-2">
            <input v-model="password2" type="password"
              class="block w-full rounded-xl bg-white px-3.5 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 placeholder:text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 transition-all duration-150">
          </div>
        </div>
        <button
          class="mt-7 block w-full rounded-xl bg-blue-three btn-hover-dark z-3 px-3.5 py-2 text-white cursor-pointer">Изменить</button>
      </form>
      <button v-on:click="logout()"
        class="mt-7 block w-full rounded-xl bg-red-400 hover:bg-red-500 transition-all duration-250 z-3 px-3.5 py-2 text-white cursor-pointer">Выйти</button>
    </div>
  </div>
</template>

<script>
import { useCommonStore } from '@/stores';
import axios from 'axios';

export default {
  name: 'MyAccountView',
  methods: {
    logout() {
      axios.defaults.headers.common['Authorization'] = ""

      localStorage.removeItem("token")
      localStorage.removeItem("username")
      localStorage.removeItem("userId")

      const commonStore = useCommonStore()
      commonStore.removeToken()

      this.$router.push('/')
    }
  },
}
</script>

<style></style>
