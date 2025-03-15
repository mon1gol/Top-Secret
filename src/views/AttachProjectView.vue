<template>
  <div class="p-10 pt-40">
    <div class="text-6xl font-bold text-center">Прикрепить проект</div>
    <h2 class="mt-10 text-3xl text-center">Выберите соревнования</h2>

    <div v-if="!tournaments.length" class="flex justify-center mt-40 flex-col items-center gap-10">
      <h1 class="text-2xl text-gray-500">На данный момент у вас нет активных мероприятий</h1>
      <router-link to="/">
        <button class="text-white bg-blue-four hover:opacity-90 cursor-pointer rounded-2xl px-10 py-5">К соренованиям</button>
      </router-link>
    </div>

    <div class="mt-40 grid grid-cols-3 justify-items-center gap-y-10">
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
  name: 'AttachProjectView',
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
