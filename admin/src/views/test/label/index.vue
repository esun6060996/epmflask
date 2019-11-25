<template>
    <d2-container>
        <template slot="header">
            Page 2 Get:api/labes
        </template>
        <el-checkbox :indeterminate="isIndeterminate" v-model="checkAll" @change="handleCheckAllChange">全选</el-checkbox>
        <div style="margin: 15px 0;"></div>
        <el-checkbox-group v-model="checkList" @change="handleCheckedChange">     
            <el-checkbox  v-for="(item) in labels" 
                    :label="item"   
                    :key="item"  
            >
            {{item}}
        </el-checkbox>
        </el-checkbox-group>

    </d2-container>
</template>

<script>
import request from '@/plugin/axios'
export default {
      data() {
        return {
                checkAll: true,
                labels:[],
                checkList: [],
                isIndeterminate: false
            }
        },
        name: 'label',
        created() {
            request({
                url: '/labels?group=projects',
                method: 'get'
                }).then(res => {
                this.labels= res
                this.checkList=this.labels//默认全选               
            });
        },
        methods: {
            handleCheckAllChange(event) {
                this.checkList = event ? this.labels : []
                this.isIndeterminate = false
            },
            handleCheckedChange(value) {
                let checkedCount = value.length
                this.checkAll = checkedCount === this.labels.length
                this.isIndeterminate = checkedCount > 0 && checkedCount < this.labels.length
            }
        }
}
</script>
