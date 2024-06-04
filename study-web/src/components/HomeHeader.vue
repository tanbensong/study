<template>
  <div>
    <div class="study-header">
      <div :class="headerClass">
        <div class="row">
          <div class="col-md-12">
            <div class="pull-left study-logo">
              <img src="@/assets/home-logo.png" alt="home-logo">
            </div>
            <div class="pull-right">
              <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect"
                background-color="#1ec4c4" text-color="#fff" active-text-color="#ff9800">
                <el-menu-item index="1">首页</el-menu-item>
                <el-submenu index="2">
                  <template slot="title">运维笔录</template>
                  <el-menu-item index="2-1">服务器运维</el-menu-item>
                  <el-menu-item index="2-2">网站运维</el-menu-item>
                  <el-menu-item index="2-3">数据库运维</el-menu-item>
                  <el-menu-item index="2-3">自动化运维</el-menu-item>
                  <el-menu-item index="2-3">服务器监控</el-menu-item>
                  <el-menu-item index="2-3">智能化运维</el-menu-item>
                </el-submenu>
                <el-menu-item index="3" disabled>个人中心</el-menu-item>
                <el-menu-item index="4" disabled>笔录管理</el-menu-item>
                <el-menu-item index="5" disabled>发布笔录</el-menu-item>
              </el-menu>
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
  data() {
    return {
      activeIndex: '1',
    };
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
<style scoped>
.study-logo img {
  max-height: 60px;
}
</style>
