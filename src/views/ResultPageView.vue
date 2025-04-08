<template>
  <div class="pt-40">
    <AppContainer>
      <h1 class="text-6xl font-bold text-center mb-15">{{ team_result.name }}</h1>

      <table class="w-full table-auto bg-blue-one rounded-2xl">
        <thead>
          <tr class="odd:bg-blue-600/30 odd:rounded-2xl even:bg-gray-950">
            <th class="p-5 rounded-tl-2xl">№</th>
            <th class="p-5">Критерий</th>
            <th class="p-5">Баллы</th>
            <th class="p-5 rounded-tr-2xl">Максимальный балл</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(criteria, index) in team_result.assessments" :key="index">
            <td class="p-5 text-center">{{ index }}</td>
            <td class="p-5 text-center">{{ criteria.criterion }}</td>
            <td class="p-5 text-center">{{ criteria.score }}</td>
            <td class="p-5 text-center">{{ criteria.max_score }}</td>
          </tr>
        </tbody>
        <tfoot class="bg-blue-600/10">
          <tr>
            <td class="p-5 text-center rounded-bl-2xl">Всего баллов</td>
            <td class="p-5 text-center"></td>
            <td class="p-5 text-center"></td>
            <td class="p-5 text-center rounded-br-2xl">{{ sumCriteria() }}</td>
          </tr>
        </tfoot>
      </table>
    </AppContainer>
  </div>
</template>
<script>
import AppContainer from '@/components/AppContainerComponent.vue';
import axios from 'axios';


export default {
  name: "ResultPageView",
  components:{
    AppContainer,
  },
  data() {
    return {
      team_result: {
        assessments: []
      }
    }
  },
  mounted() {
    this.getTeamResults()
  },
  methods: {
    getTeamResults() {
      const username = localStorage.getItem('username')
      const id_team = this.$route.params.id_team

      axios
        .get(`/api/v1/team-results/${username}/${id_team}/`)
        .then((response) => {
          this.team_result = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    sumCriteria(){
      if (!this.team_result || !this.team_result.assessments) {
        return 0;
      }

      let sum = 0;
      this.team_result.assessments.forEach(criteria => {
        sum += criteria.score;
      });

      return sum;
    }
  },
}
</script>
