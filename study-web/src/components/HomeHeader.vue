<template>
  <div>
    <div class="study-header">
      <div :class="headerClass">
        <div class="row">
          <div class="col-md-12">
            <div class="pull-left study-logo"  v-if="windowWidth > 770">
              <img src="@/assets/home-logo.png" alt="home-logo">
            </div>
            <div class="pull-right">
              <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect"
                background-color="#1ec4c4" text-color="#fff" active-text-color="#ff9800">
                <el-menu-item index="1"><i class="fa fa-home fa-fw"></i> 首页</el-menu-item>
                <el-submenu index="2">
                  <template slot="title">运维笔录</template>
                  <el-menu-item index="2-1">服务器运维</el-menu-item>
                  <el-menu-item index="2-2">网站运维</el-menu-item>
                  <el-menu-item index="2-3">数据库运维</el-menu-item>
                  <el-menu-item index="2-3">自动化运维</el-menu-item>
                  <el-menu-item index="2-3">服务器监控</el-menu-item>
                  <el-menu-item index="2-3">智能化运维</el-menu-item>
                </el-submenu>
                <el-submenu index="3">
                  <template slot="title">在线案例</template>
                  <el-menu-item index="3-1">shell 脚本</el-menu-item>
                  <el-menu-item index="3-2">python 脚本</el-menu-item>
                </el-submenu>
                <el-menu-item index="4" disabled>个人中心</el-menu-item>
                <el-menu-item index="5" class="with-divider"><i class="fa fa-user fa-fw"></i> 登陆·注册</el-menu-item>
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
      windowWidth: window.innerWidth,
    };
  },
  computed: {
    headerClass() {
      return {
        'container': window.innerWidth > 1000, // 根据屏幕宽度动态切换的样式类
        'container-fluid': window.innerWidth <= 1000, // 根据屏幕宽度动态切换的样式类
      };
    },
  },
  mounted() {
    window.addEventListener('resize', this.handleResize);
  },
  methods: {
    handleResize() {
      this.windowWidth = window.innerWidth;
    },
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.handleResize);
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.study-logo img {
  max-height: 60px;
}

.fa {
  color: #fff;
}

.with-divider {
  border-left: #e0e0e0 1px solid;
}
</style>
