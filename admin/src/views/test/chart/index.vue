<template>
  <d2-container>
    <template slot="header">图表</template>
    <div>
        <ve-line :data="chartData" v-bind="pubSetting"></ve-line>
    </div>
  </d2-container>
</template>

<script>
    import request from '@/plugin/axios'
    import makeSeqData from '@/api/makeSeqData'

    export default {
          data () {
                return {
                    chartData: {
                        columns: [],
                        rows: []
                    }
                }
            },
            created() {
                request({
                    url: '/time',
                    method: 'get'
                }).then(res => {
                    //console.log(res);
                    this.chartData.columns=res.columns;
                    this.chartData.rows=makeSeqData(res.rows);
                 });
            },
    }
</script>

<style lang="scss" scoped>

</style>
