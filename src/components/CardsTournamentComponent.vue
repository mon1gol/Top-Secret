<template>
  <div class="p-10">
    <div v-if="!tournaments.length" class="flex justify-center mt-30 flex-col items-center space-y-10">
      <h1 class="text-2xl text-gray-500">На данный момент мероприятий нет</h1>
      <router-link v-if="!tournaments.length && !isHome" to="/">
        <button class="text-white bg-blue-four hover:opacity-90 cursor-pointer rounded-2xl px-10 py-5">К соренованиям</button>
      </router-link>
    </div>


    <div v-else class="mt-10 grid lg:grid-cols-4 md:grid-cols-3 justify-items-center gap-10">
      <router-link :to="linkIncrement + tournament.get_absolute_url" class="bg-blue-200 shadow-sm overflow-hidden rounded-xl"
        v-for="tournament in tournaments" :key="tournament.id">
        <img class="bg-blue-two h-100 w-100 object-cover" :src="tournament.get_image">
        <div class="p-10 text-xl">{{ tournament.name }}</div>
      </router-link>
    </div>
  </div>
</template>
<script>
export default {
  name: "CardsTournamentComponent",
  props:{
    tournaments: Array,
    linkIncrement: String,
    isHome: Boolean,
  }
}
</script>
