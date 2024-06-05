<template>
  <div>
    <HomeHeaderVue/>
    <HomeCount/>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  components: {
    HomeHeaderVue: () => import('@/components/HomeHeader.vue'),
    HomeCount: () => import('@/components/HomeCount.vue'),
  }
}
</script>
<style>

</style>
