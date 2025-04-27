  <template>
    <main class="bg-white-one">
      <AppContainer>
        <div class="pt-40 text-6xl font-bold text-center">Соревнования</div>
        <div class="mt-30 bg-blue-one p-5 w-full flex flex-wrap justify-center gap-x-20 relative rounded-xl shadow-sm">
          <div class="px-10 h-full cursor-pointer category-btn-hover-dark relative z-5"
            @click="getCategoryBySlug('all')"
            :class="{ 'bg-blue-two rounded-xl': activeCategory === 'all' }">
            Все
          </div>
          <div class="px-10 h-full cursor-pointer category-btn-hover-dark relative z-5"
            @click="getCategoryBySlug('hackathons')"
            :class="{ 'bg-blue-two rounded-xl': activeCategory === 'hackathons' }">
            Хакатоны
          </div>
          <div class="px-10 h-full cursor-pointer category-btn-hover-dark relative z-5"
            @click="getCategoryBySlug('olympiads')"
            :class="{ 'bg-blue-two rounded-xl': activeCategory === 'olympiads' }">
            Олимпиады
          </div>
          <div class="px-10 h-full cursor-pointer category-btn-hover-dark relative z-5"
            @click="getCategoryBySlug('project_work')"
            :class="{ 'bg-blue-two rounded-xl': activeCategory === 'project_work' }">
            Проектная деятельность
          </div>
        </div>

        <CardsTournamentComponent :tournaments="this.latestTournaments" :linkIncrement="''" :isHome="true" />
      </AppContainer>
    </main>
  </template>

<script>
import AppContainer from '@/components/AppContainerComponent.vue';
import CardsTournamentComponent from '@/components/CardsTournamentComponent.vue';
import axios from 'axios';


export default {
  name: 'HomeView',
  components: {
    CardsTournamentComponent,
    AppContainer
  },
  data() {
    return {
      latestTournaments: [],
      activeCategory: 'all',
    };
  },
  mounted() {
    this.getLatestTournaments();
    document.title = 'Home';
  },
  methods: {
    getLatestTournaments() {
      axios
        .get('/api/v1/latest-tournaments/')
        .then((response) => {
          const currentDate = new Date().toISOString().split('T')[0];
          const tournament_list = response.data;

          this.latestTournaments = tournament_list.filter((tournament) => {
            return tournament.rules.date_start > currentDate;
          });
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getCategoryBySlug(slug) {
      this.activeCategory = slug;
      if (slug == 'all') {
        this.getLatestTournaments()
      }
      else {
        axios
          .get(`/api/v1/tournaments/${slug}/`)
          .then((response) => {
            const currentDate = new Date().toISOString().split('T')[0];
            const tournament_list = response.data.tournaments;

            this.latestTournaments = tournament_list.filter((tournament) => {
              return tournament.rules.date_start > currentDate;
            });
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
};
</script>

<style></style>
