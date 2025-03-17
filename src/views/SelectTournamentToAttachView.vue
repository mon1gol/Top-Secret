<template>
  <div class="bg-white-one h-lvh w-lvw p-20">
    <div class="flex gap-15 justify-between">
      <div>
        <h1 class="text-6xl">{{ tournament.name }}</h1>
        <div class="mt-10 flex flex-col gap-2">
          <div>Дата начала: </div>
          <div>Дата окончания: </div>
        </div>

        <div class="mt-10">
          <form @submit.prevent="submitForm" class="flex flex-col gap-5 w-3/4">
            <div>
              <label for="username" class="block text-sm/6 font-semibold text-black">Ссылка</label>
              <div class="mt-2">
                <textarea v-model="project_link" placeholder="Введите здесь ссылку на ваш проект" type="text"
                  class="block w-full rounded-xl bg-white px-3.5 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 placeholder:text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 transition-all duration-150"></textarea>
              </div>
            </div>
            <div>
              <label for="file" class="block text-sm/6 font-semibold text-black">Короткое видео демонстрации работы</label>
              <div class="mt-2">
                <input
                  ref="fileInput"
                  @change="handleFileChange"
                  placeholder="Введите" type="file"
                  class="file:cursor-pointer mt-1 block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
                >
              </div>
            </div>
            <button class="mt-7 block w-full rounded-xl bg-blue-three btn-hover-dark z-3 px-3.5 py-2 text-white cursor-pointer">
              Прикрепить проект
            </button>
            <div class="text-red-500 text-center" v-if="errors.length">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>
          </form>
        </div>
      </div>

      <div class="">
        <img class="h-100 w-100 object-cover shadow-2xl" :src="tournament.get_image" :alt="tournament.name">
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'SelectTournamentToAttachView',
  data() {
    return {
      tournament: {},
      previous_project: {},
      username: localStorage.getItem('username'),
      file_name: null,
      project_link: '',
      errors: [],
    }
  },
  mounted() {
    this.getTournament()
  },
  methods: {
    getTournament() {
      const category_slug = this.$route.params.category_slug
      const tournament_slug = this.$route.params.tournament_slug

      axios
        .get(`/api/v1/tournaments/${category_slug}/${tournament_slug}/`)
        .then(response => {
          this.tournament = response.data
          document.title = this.tournament.name
        })
        .catch(error => {
          console.log(error)
        })
    },
    getPreviousProjects(){
      const tournament_slug = this.$route.params.tournament_slug

      axios
        .get(`/api/v1/projects/${tournament_slug}/${this.username}/`)
        .then(response => {
          this.previous_project = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    handleFileChange(event){
      this.errors = []
      const file = event.target.files[0]

      if (file) {
        const allowedExtensions = ["mp4"];
        const fileExtension = file.name.split(".").pop().toLowerCase();

        if (!allowedExtensions.includes(fileExtension)) {
          this.errors.push("Разрешены только файлы с расширениями: " + allowedExtensions.join(", "));
          this.file_name = null;
          this.$refs.fileInput.value = "";
          return;
        }

        const maxSize = 10 * 1024 * 1024;
        if (file.size > maxSize) {
          this.errors.push("Максимальный размер файла — 10 MB.");
          this.file_name = null;
          this.$refs.fileInput.value = "";
          return;
        }
        this.file_name = file;
      }
    },
    async submitForm(){
      this.errors = []

      if(!this.errors.length){
        const formData = {
          description: this.project_link,
          file_name: this.file_name
        }
        console.log(formData)

        const tournament_slug = this.$route.params.tournament_slug

        await axios
          .post(`/api/v1/projects/${tournament_slug}/${this.username}/`, formData, {
            headers:{
              "Content-Type": "multipart/form-data",
            }
          })
          .then((response) =>{
            if (response.status === 201) {
              this.$router.push('/attach-project')
            }
          })
          .catch(error => {
            if(error.response){
              for(const property in error.response.data){
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }

              console.log(JSON.stringify(error.response.data))
            }
            else if(error.message) {
              this.errors.push('Произошла ошибка, попробуйте позже')

              console.log(JSON.stringify(error))
            }
          })
      }
    },
  }
}
</script>
