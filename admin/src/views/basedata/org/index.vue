<template>
  <d2-container>
    <template slot="header">组织架构</template>
    <div>
        <el-tree :props="props"
                 :data="tree"
                 show-checkbox
                 @node-click="handleNodeClick"
                 >
        </el-tree>
    </div>
  </d2-container>

</template>

<script>
  import request from '@/plugin/axios'
  export default {
    data() {
          return {
              tree: [],
              props: {
                  label: 'name',
                  children: 'children'
              }
          };
      },
      created() {
          request({
              url: '/organizationunits',
              method: 'get'
          }).then(res => {
              console.log(res);
              this.tree = [res];
          });
      },
      methods: {
          handleNodeClick(data) {
              console.log(data);
          }
      }
  }
</script>
