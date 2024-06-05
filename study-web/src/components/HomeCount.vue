<template>
  <div>
    <div >
      <div class="echarts-view" style="width: 100%; height: 230px;">
        <!-- <v-chart :option="chartOptions" :autoresize="true" /> -->
      </div>
    </div>
  </div>
</template>

<script>
// import studyMixin from '@/studyMixin'


export default {
  name: "HomeCount",
  // created() {
  //   this.$options.components['v-chart'] = ECharts
  // },
  // mixins: [studyMixin],
  data() {
    return {
      chartOptions: {
        xAxis: {
          type: "category",
          data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            data: [120, 200, 150, 80, 70, 110, 130],
            type: "bar",
          },
        ],
      },
      width: "100%",
      height: "100%",
      chartId: "home-count-chart",
    };
  },
};
</script>

<style>
</style>