<template>
  <main class="bg-white-one w-lvw">
    <div class="p-5 pt-40">
      <div class="text-6xl font-bold text-center">Соревнования</div>

      <div 
        class="mt-40 grid grid-cols-3 justify-items-center gap-y-10"
        v-for="tournament in latestTournaments"
        v-bind:key="tournament.id"
      >
        <div class="bg-blue-500 size-100">
          <img class="bg-blue-two h-70" :src="tournament.get_image">
          <div class="p-5 text-2xl">{{ tournament.name }}</div>
        </div>
        
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
      latestTournaments: []
    }
  },
  components: {
    
  },
  mounted(){
    this.getLatestTournaments()
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
    }
  }
}
</script>