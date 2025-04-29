<template>
  <div class="pt-40">
    <AppContainer>
      <div class="text-6xl font-bold text-center">Прикрепить проект</div>
      <h2 class="mt-10 mb-20 text-3xl text-center">Выберите соревнование</h2>
      <CardsTournamentComponent :tournaments="this.tournaments" :linkIncrement="'/attach-project'" :isHome="false"/>
    </AppContainer>
  </div>

</template>

<script>
import AppContainer from '@/components/AppContainerComponent.vue';
import CardsTournamentComponent from '@/components/CardsTournamentComponent.vue';
import axios from 'axios';


export default {
  name: 'AttachProjectView',
  components:{
    CardsTournamentComponent,
    AppContainer
  },
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
