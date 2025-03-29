<template>
  <div class="h-lvh bg-white-one w-lvw p-20 grid grid-cols-2 gap-15">
    <div>
      <h1 class="text-6xl">{{ tournament.name }}</h1>
      <div class="mt-10">{{ tournament.description }}</div>
      <div class="mt-10 flex flex-col gap-2">
        <div>
          <div class="flex items-center">Дата начала: <div class="ml-2 bg-blue-two rounded-2xl p-1">{{ tournament_rules.date_start }}</div></div>
        </div>
        <div>
          <div class="flex items-center">Дата окончания: <div class="ml-2 bg-blue-two rounded-2xl p-1">{{ tournament_rules.date_end }}</div></div>
        </div>
        <div>В команде должно быть от {{ tournament_rules.min_members_in_team }} до {{ tournament_rules.max_members_in_team }} участников</div>
      </div>
      <router-link :to="tournament.get_absolute_url + 'submit'">
        <button class="bg-blue-four mt-10 cursor-pointer rounded-2xl px-10 py-5">Подать заявку</button>
      </router-link>
    </div>
    <div class="">
      <img class="h-100 w-150 object-cover shadow-2xl" :src="tournament.get_image" :alt="tournament.name">
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TournamentView',
  data() {
    return {
      tournament: {},
      tournament_rules: {},
    }
  },
  mounted(){
    this.getTournament()
  },
  methods: {
    getTournament(){
      const category_slug = this.$route.params.category_slug
      const tournament_slug = this.$route.params.tournament_slug

      axios
        .get(`/api/v1/tournaments/${category_slug}/${tournament_slug}/`)
        .then(response =>{
          this.tournament = response.data
          if(response.data.rules){this.tournament_rules = response.data.rules}
          document.title = this.tournament.name
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
