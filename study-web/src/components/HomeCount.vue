<template>
  <div>
    <div class="echarts-view">
      <v-chart :options="chartOptions" :autoresize="true" :id="chartId" :style="{ height, width }"></v-chart>
    </div>
  </div>
</template>

<script>
// import ECharts from 'vue-echarts'
// import { Line } from 'pyecharts.globals'
export default {
  name: "HomeCount",
  // components: {
  //   'v-chart': ECharts
  // },
  data() {
    return {
      chartOptions: {
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            data: [150, 230, 224, 218, 135, 147, 260],
            type: 'line'
          }
        ]
      },
      width: "100%",
      height: "100%",
      chartId: "home-count-chart",
    };
  },
}
</script>

<style>

</style>