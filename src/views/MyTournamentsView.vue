<template>
  <div class="p-10 pt-40">
    <div class="text-6xl font-bold text-center">Мои соревнования</div>

    <div
      class="mt-30 bg-blue-one p-5 w-full flex flex-wrap justify-center gap-x-20 gap-y-5 relative rounded-xl shadow-sm">
      <div class="px-10 h-full cursor-pointer category-btn-hover-dark relative z-10" @click="getTournamentsByStatus('upcoming')">
        Предстоящие
      </div>
      <div class="px-10 h-full cursor-pointer category-btn-hover-dark relative z-10"
        @click="getTournamentsByStatus('comingnow')">
        Идут в данный момент
      </div>
      <div class="px-10 h-full cursor-pointer category-btn-hover-dark relative z-10"
        @click="getTournamentsByStatus('completed')">
        Завершенные
      </div>
    </div>

    <div v-if="!tournaments.length" class="flex justify-center mt-30">
      <h1 class="text-2xl text-gray-500">На данный момент мероприятий нет</h1>
    </div>

    <div v-else class="mt-10 grid grid-cols-3 justify-items-center gap-y-10">
      <router-link :to="tournament.get_absolute_url" class="bg-blue-200 size-100 shadow-sm overflow-hidden rounded-xl"
        v-for="tournament in tournaments" :key="tournament.id">
        <img class="bg-blue-two h-70 w-100 object-cover" :src="tournament.get_image">
        <div class="p-5 text-2xl">{{ tournament.name }}</div>
      </router-link>
    </div>
  </div>
</template>
<script>
import axios from 'axios';


export default {
  name: "MyTournamentsView",
  data() {
    return {
      tournaments:[],
      username: localStorage.getItem("username"),
    }
  },
  mounted() {
    this.getTournamentsByStatus('comingnow')
  },
  methods: {
    getTournamentsByStatus(status_slug){
      axios
          .get(`/api/v1/tournaments/status/${status_slug}/${this.username}/`)
          .then((response) => {
            this.tournaments = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
    },
  },
}
</script>
