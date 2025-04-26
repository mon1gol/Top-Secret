<template>
  <div class="pt-40">
    <AppContainer>
      <div class="text-6xl font-bold text-center">Мои соревнования</div>
      <div
        class="mt-30 bg-blue-one p-5 w-full flex flex-wrap justify-center gap-x-20 gap-y-5 relative rounded-xl shadow-sm">
        <div class="px-10 h-full cursor-pointer category-btn-hover-dark relative z-10"
          @click="getTournamentsByStatus('upcoming')"
          :class="{ 'bg-blue-two rounded-xl': activeCategory === 'upcoming' }"
        >
          Предстоящие
        </div>
        <div class="px-10 h-full cursor-pointer category-btn-hover-dark relative z-10"
          @click="getTournamentsByStatus('comingnow')"
          :class="{ 'bg-blue-two rounded-xl': activeCategory === 'comingnow' }"
        >
          Идут в данный момент
        </div>
        <div class="px-10 h-full cursor-pointer category-btn-hover-dark relative z-10"
          @click="getTournamentsByStatus('completed')"
          :class="{ 'bg-blue-two rounded-xl': activeCategory === 'completed' }"
        >
          Завершенные
        </div>
      </div>
      <CardsTournamentComponent :tournaments="this.tournaments" :linkIncrement="''" :isHome="false"/>
    </AppContainer>
  </div>
</template>

<script>
import AppContainer from '@/components/AppContainerComponent.vue';
import CardsTournamentComponent from '@/components/CardsTournamentComponent.vue';
import axios from 'axios';


export default {
  name: "MyTournamentsView",
  components:{
    CardsTournamentComponent,
    AppContainer
  },
  data() {
    return {
      tournaments:[],
      username: localStorage.getItem("username"),
      activeCategory: 'comingnow'
    }
  },
  mounted() {
    this.getTournamentsByStatus('comingnow')
  },
  methods: {
    getTournamentsByStatus(status_slug){
      this.activeCategory = status_slug;

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
