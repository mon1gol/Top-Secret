<template>
  <main class="bg-white-one w-lvw">
    <div class="p-10 pt-40">
      <div class="text-6xl font-bold text-center">Соревнования</div>

      <div class="mt-30 bg-blue-one p-5 w-full flex flex-wrap justify-center gap-x-20 gap-y-5 relative rounded-xl shadow-sm">
        <div class="px-10 h-full cursor-pointer category-btn-hover-dark relative z-10">Все</div>
        <div class="px-10 h-full cursor-pointer category-btn-hover-dark relative z-10">Хакатоны</div>
        <div class="px-10 h-full cursor-pointer category-btn-hover-dark relative z-10">Олимпиады</div>
      </div>

      <div class="mt-10 grid grid-cols-3 justify-items-center gap-y-10">
        <router-link :to="tournament.get_absolute_url" class="bg-blue-500 size-100 shadow-sm"
          v-for="tournament in latestTournaments"
          v-bind:key="tournament.id"
        >
          <img class="bg-blue-two h-70 w-100 object-cover" :src="tournament.get_image">
          <div class="p-5 text-2xl">{{ tournament.name }}</div>
        </router-link>
      </div>
    </div>
  </main>
</template>

<script>
import axios from 'axios';

export default{
  name: 'HomeView',
  data() {
    return{
      latestTournaments: [],
    }
  },
  components: {

  },
  mounted(){
    this.getLatestTournaments()
    document.title = 'Home'
  },
  methods: {
    getLatestTournaments(){
      axios
        .get('/api/v1/latest-tournaments/')
        .then(Response =>{
          this.latestTournaments = Response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
  }
}
</script>
