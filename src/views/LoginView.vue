<template>
  <div class="gradient-blue flex flex-col h-lvh w-lvw items-center justify-center">
    <h1 class="mt-20 mb-10 text-5xl font-medium">Вход</h1>
    <div class="h-120 w-100 px-10 py-15 rounded-xl">
      <form @submit.prevent="submitForm" class="flex flex-col gap-5">
        <div>
          <label for="username" class="block text-sm/6 font-semibold text-black">Логин</label>
          <div class="mt-2">
            <input v-model="username" placeholder="Введите" type="text" class="block w-full rounded-xl bg-white px-3.5 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 placeholder:text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 transition-all duration-150">
          </div>
        </div>
        <div>
          <label for="password" class="block text-sm/6 font-semibold text-black">Пароль</label>
          <div class="mt-2">
            <input v-model="password" placeholder="Введите" type="password" class="block w-full rounded-xl bg-white px-3.5 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 placeholder:text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 transition-all duration-150">
          </div>
        </div>
        <button class="mt-7 block w-full rounded-xl bg-blue-three btn-hover-dark z-3 px-3.5 py-2 text-white cursor-pointer">Войти</button>
        <!-- <div class="text-red-500 text-center" v-if="errors.length">
          <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
        </div> -->
        <hr>
          <div class="text-center">Или <router-link class="text-blue-700 border-b-1 hover:text-blue-900" to="/sign-up">зарегестрируйтесь</router-link></div>
      </form>
    </div>
  </div>
</template>
<script>
export default {
  name: "LoginView",
}
</script>
<style>

</style>
