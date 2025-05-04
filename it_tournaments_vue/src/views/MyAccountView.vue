<template>
  <div class="gradient-blue flex flex-col h-lvh w-lvw items-center justify-center">
    <h1 class="text-6xl font-bold text-center">Профиль</h1>
    <div class="h-120 w-100 px-10 py-15 rounded-xl">
      <form @submit.prevent="submitForm" class="flex flex-col gap-5">
        <div>
          <label for="username" class="block text-sm/6 font-semibold text-black">Логин</label>
          <div class="mt-2">
            <input type="text" :value="this.username" disabled
              class="block w-full rounded-xl bg-white px-3.5 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 placeholder:text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 transition-all duration-150">
          </div>
        </div>
        <div>
          <label for="passwordold" class="block text-sm/6 font-semibold text-black">Старый пароль</label>
          <div class="mt-2">
            <input v-model="passwordold" type="password" placeholder="Введите"
              class="block w-full rounded-xl bg-white px-3.5 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 placeholder:text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 transition-all duration-150">
          </div>
        </div>
        <div>
          <label for="password1" class="block text-sm/6 font-semibold text-black">Новый пароль</label>
          <div class="mt-2">
            <input v-model="password1" type="password" placeholder="Введите"
              class="block w-full rounded-xl bg-white px-3.5 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 placeholder:text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 transition-all duration-150">
          </div>
        </div>
        <button
          class="mt-7 block w-full rounded-xl bg-blue-three btn-hover-dark z-3 px-3.5 py-2 text-white cursor-pointer">Изменить</button>
      </form>
      <button v-on:click="logout()"
        class="mt-7 block w-full rounded-xl bg-red-400 hover:bg-red-500 transition-all duration-250 z-3 px-3.5 py-2 text-white cursor-pointer">
        Выйти
      </button>
      <div class="text-red-500 text-center" v-if="errors.length">
        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { useCommonStore } from '@/stores';
import { toast } from 'vue-sonner'
import axios from 'axios';

export default {
  name: 'MyAccountView',
  data() {
    return {
      username: localStorage.getItem('username'),
      passwordold: '',
      password1: '',
      errors: [],
    }
  },
  methods: {
    toast,

    logout() {
      axios.defaults.headers.common['Authorization'] = ""

      localStorage.removeItem("token")
      localStorage.removeItem("username")
      localStorage.removeItem("userId")

      const commonStore = useCommonStore()
      commonStore.removeToken()

      this.$router.push('/')
    },

    submitForm() {
      const formData = {
        "current_password": this.passwordold,
        "new_password": this.password1,
      }

      axios
          .post("/auth/users/set_password/", formData)
          .then(response => {
            if (response.status === 201) {
              toast('Пароль успешно изменен', {})
            }
          })
          .catch(error => {
            toast('Не удалось изменить пароль', {
              style: {
                background: '#fda4af'
              },
            })
            if (error.response) {
              this.errors.push(error.response)
            }
            else if (error.message) {
              this.errors.push('Произошла ошибка, попробуйте позже')

              console.log(JSON.stringify(error))
            }
          })
    }
  },
}
</script>

<style></style>
