<template>
  <div class="about pt-40">
    <AppContainer>
      <h1>О сайте</h1>
    </AppContainer>
  </div>
</template>

<script>
import AppContainer from '@/components/AppContainerComponent.vue';

export default{
  name: 'AboutView',
  components: {
    AppContainer,
  },
  mounted(){
    document.title = 'About'
  }
}
</script>

<style>

</style>
