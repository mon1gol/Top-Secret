<template>
  <div class="p-10 pt-40">
    <div class="text-6xl font-bold text-center">Прикрепить проект</div>

    <div class="mt-10 grid grid-cols-3 justify-items-center gap-y-10">
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
    }
  },
  mounted() {
    this.getTournamentsByStatus('comingnow')
  },
  methods: {
    getTournamentsByStatus(status_slug){
      axios
          .get(`/api/v1/tournaments/status/${status_slug}/`)
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
