import { defineStore } from 'pinia'
import { ref } from 'vue'


export const useCommonStore = defineStore('commonStore', () => {
  const isAuthenticated = ref(false)
  const token = ref('')

  function initializeStore(){
    if(localStorage.getItem('token')){
      token.value = localStorage.getItem('token')
      isAuthenticated.value = true
    } else {
      token.value = ''
      isAuthenticated.value = false
    }
  }

  function setToken(newToken){
    token.value = newToken
    isAuthenticated.value = true
  }

  function removeToken(){
    token.value = ''
    isAuthenticated.value = false
  }

  return{
    token,
    isAuthenticated,
    initializeStore,
    setToken,
    removeToken,
  }
})
