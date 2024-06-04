<template>
  <div>
    <div class="study-header">
      <div :class="headerClass">
        <div class="row">
          <div class="col-md-12">
            <div class="pull-left">
              <img src="@/assets/home-logo.png" alt="home-logo">
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeHeader',
  props: {
    msg: String
  },
  computed: {
    headerClass() {
      return {
        'container': window.innerWidth > 768, // 根据屏幕宽度动态切换的样式类
        'container-fluid': window.innerWidth <= 768 // 根据屏幕宽度动态切换的样式类
      };
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
