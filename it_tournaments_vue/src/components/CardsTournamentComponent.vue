<template>
  <div>
    <div v-if="isLoading" class="mt-10 grid justify-items-center gap-10 md:grid-cols-2 lg:grid-cols-4">
      <div v-for="index in 10" :key="index" class="">
        <Skeleton class="h-100 w-85 rounded-xl" />
      </div>
    </div>

    <div v-else-if="!isLoading && !this.tournaments.length" class="mt-30 flex flex-col items-center justify-center space-y-10">
      <h1 class="text-2xl">На данный момент мероприятий нет</h1>
      <router-link v-if="!tournaments.length && !isHome" to="/">
        <button class="text-white bg-blue-four hover:opacity-90 cursor-pointer rounded-2xl px-10 py-5">К соренованиям</button>
      </router-link>
    </div>

    <div v-else class="mt-10 grid justify-items-center gap-10 md:grid-cols-2 lg:grid-cols-4">
      <router-link :to="linkIncrement + tournament.get_absolute_url" class="overflow-hidden rounded-xl bg-blue-200 shadow-sm"
        v-for="tournament in tournaments" :key="tournament.id">
        <img class="bg-blue-two h-100 w-100 object-cover" :src="tournament.get_image">
        <div class="pb-10 pt-5 px-10 text-xl">{{ tournament.name }}</div>
      </router-link>
    </div>
  </div>
</template>
<script>
import { Skeleton } from '@/components/ui/skeleton'

export default {
  name: "CardsTournamentComponent",
  props:{
    tournaments: Array,
    linkIncrement: String,
    isHome: Boolean,
  },
  components: {
    Skeleton
  },
  data() {
    return {
      isLoading: true
    };
  },
  created(){
    this.fetchTournaments()
  },
  methods:{
    fetchTournaments(){
      setTimeout(() => {
        this.isLoading = false
      }, 2000);
    }
  }
}
</script>
