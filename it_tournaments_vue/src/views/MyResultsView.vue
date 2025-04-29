<template>
  <div class="pt-40">
    <AppContainer>
      <div class="text-6xl font-bold text-center mb-15">Результаты соревнований</div>
        <div class="w-full space-y-10">
          <div v-for="result in teams_result" :key="result.id">
            <div v-if="result.assessments.length" class="bg-blue-one px-10 py-5 rounded-xl">
              <h1 class="text-2xl">{{result.name}}</h1>
              <h2>{{result.tournament}}</h2>
              <div class="flex justify-end">
                <router-link :to="'my-results' + result.get_absolute_url" class="hover:underline">Доступны результаты ➡️</router-link>
              </div>
            </div>
          </div>
        </div>
    </AppContainer>
  </div>
</template>
<script>
import AppContainer from '@/components/AppContainerComponent.vue';
import axios from 'axios';


export default {
  name: 'MyResultsView',
  data() {
    return {
      username: localStorage.getItem('username'),
      teams_result: []
    }
  },
  components:{
    AppContainer,
  },
  mounted() {
    this.getTeamResults();
  },
  methods: {
    getTeamResults() {
      axios
        .get(`/api/v1/team-results/${this.username}/`)
        .then((response) => {
          this.teams_result = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
}
</script>
