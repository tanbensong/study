<template>
  <div>
    <HomeHeaderVue/>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  components: {
    HomeHeaderVue: () => import('@/components/HomeHeader.vue')
  }
}
</script>
<style>

</style>
