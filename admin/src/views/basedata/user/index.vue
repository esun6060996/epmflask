<template>
    <d2-container>
        <template slot="header">
            Page 2 Get:api/Users
        </template>
            <d2-crud
            ref="d2Crud"
            :columns="columns"
            :data="data"
            :options="options"
            :pagination="pagination"
            @pagination-current-change="paginationCurrentChange"/>
    </d2-container>
</template>

<script>
import request from '@/plugin/axios'
export default {
  data() {
    return {
            columns:[
                {
                title: '登录名',
                key: 'username',
                width: '180'
                },
                {
                title: '电子邮件',
                key: 'emailAddress'
                },
                {
                title: '电话',
                key: 'phoneNumber'
                },
                {
                title: '姓名',
                key: 'name'
                },
                {
                title: 'QQ',
                key: 'qq'
                }
            ],
            data:[],
            loading: false,
            options: {
                border: true,
                stripe: true,
                //height: '600'
            },
            pagination: {
                currentPage: 5,
                pageSize: 10,
                total: 20
            }
        }
    },
    name: 'user',
    mounted () {
        this.fetchData()
    },
    created() {
        request({
            url: '/users',
            method: 'get'
        }).then(res => {
            console.log(res);
            this.data= res.items;
            this.pagination.currentPage=res._meta.page;
            this.pagination.pageSize=res._meta.per_page;
            this.pagination.total=res._meta.total_items;    
        });
    },
    methods: {
        paginationCurrentChange (currentPage) {
        this.pagination.currentPage = currentPage
        this.fetchData()
        },
        fetchData () {
        this.loading = true
        BusinessTable1List({
            ...this.pagination
        }).then(res => {
            this.data = res.list
            this.pagination.total = res.page.total
            this.loading = false
        }).catch(err => {
            console.log('err', err)
            this.loading = false
        })
        }
    }
    
}
</script>
