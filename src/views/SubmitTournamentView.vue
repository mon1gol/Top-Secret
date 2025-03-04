<template>
  <div class="pt-30 flex flex-col items-center">
    <h1 class="mb-25 text-5xl font-medium">{{ tournament.name }}</h1>
    <form @submit.prevent="submitForm" class="w-1/3">
      <div>
        <label for="username" class="block text-sm/6 font-semibold text-black">Название команды</label>
        <div class="mt-2">
          <input v-model="team_name" placeholder="Введите" type="text"
            class="block w-full rounded-xl bg-white px-3.5 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 placeholder:text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 transition-all duration-150">
        </div>
      </div>

      <div class="mt-15 mb-5 flex justify-between items-center">
        <h1 class="text-2xl font-medium">Участники</h1>
        <button type="button" v-on:click="appendMember()" class="bg-blue-one py-2 px-4 rounded-xl cursor-pointer">Добавить</button>
      </div>

      <div
        v-for="(member, index) in members"
        :key="index"
      >
        <label :for="'nickname-' + index" class="mt-2 block text-sm/6 font-semibold text-black">Никнейм</label>
        <div class="mt-2 flex justify-between space-x-5">
          <input
            :id="'nickname' + index"
            v-model="members[index]"
            placeholder="Введите" type="text" list="search-nicknames"
            class="block w-full rounded-xl bg-white px-3.5 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 placeholder:text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 transition-all duration-150">
            <datalist id="search-nicknames">
              <option v-for="user in allUsers" :key="user.id" :value="user.username">{{ user.username }}</option>
            </datalist>
            <button type="button" v-on:click="removeMember(index)" class="bg-blue-one py-2 px-4 rounded-xl cursor-pointer">Удалить</button>
        </div>
      </div>

      <button
        class="mt-7 block w-full rounded-xl bg-blue-three btn-hover-dark z-3 px-3.5 py-2 text-white cursor-pointer">Подать заявку</button>
      <div class="text-red-500 text-center" v-if="errors.length">
        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';


export default {
  name: 'SubmitTournamentView',
  data() {
    return {
      tournament: {},
      allUsers:[],
      team_name: '',
      members: [],
      description: '',
      errors: [],
    }
  },
  mounted() {
    this.getTournament()
    this.getUsernames()
  },
  methods: {
    getTournament(){
      const category_slug = this.$route.params.category_slug
      const tournament_slug = this.$route.params.tournament_slug

      axios
        .get(`/api/v1/tournaments/${category_slug}/${tournament_slug}/`)
        .then(Response =>{
          this.tournament = Response.data
          document.title = this.tournament.name
        })
        .catch(error => {
          console.log(error)
        })
    },
    getUsernames(){
      axios
        .get(`/api/v1/users-list/`)
        .then(Response =>{
          this.allUsers = Response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    appendMember(){
      this.members.push('')
    },
    removeMember(index){
      this.members.splice(index, 1)
    },
    submitForm(){
      this.errors = []

      if(this.members.length === 0){
        this.errors.push('Недостаточно участников для создания команды')
      }

      const emptyNames = this.members.filter(member => !member.trim());

      if(emptyNames.length > 0){
        this.errors.push('Один или несколько участников не заполнены')
      }

      if(!this.errors.length){
        const formData = {
          name: this.team_name,
          description: this.description,
          usernames: this.members,
          id_tournament: this.tournament.id
        }

        const category_slug = this.$route.params.category_slug
        const tournament_slug = this.$route.params.tournament_slug

        axios
          .post(`/api/v1/tournaments/${category_slug}/${tournament_slug}/teams/`, formData)
          .then(
            this.$router.push('/')
          )
          .catch(error => {
            if(error.Response){
              for(const property in error.Response.data){
                this.errors.push(`${property}: ${error.Response.data[property]}`)
              }

              console.log(JSON.stringify(error.Response.data))
            }
            else if(error.message) {
              this.errors.push('Произошла ошибка, попробуйте позже')

              console.log(JSON.stringify(error))
            }
          })
      }
    }
  },
}
</script>
