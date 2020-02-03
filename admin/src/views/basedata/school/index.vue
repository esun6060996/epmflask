<template>
    <d2-container>
        <template slot="header">
            学校列表:api/Schools
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
  data () {
    return {
      columns: [
        {
          title: 'ID号',
          key: 'id',
          width: '180'
        },
        {
          title: '全称',
          key: 'fullname'
        },
        {
          title: '简称',
          key: 'name'
        },
        {
          title: '标签',
          key: 'label'
        },
        {
          title: '类别',
          key: 'organizationunit_id'
        }
      ],
      data: [],
      loading: false,
      options: {
        border: true,
        stripe: true
        // height: '600'
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
  created () {
    request({
      url: '/schools',
      method: 'get'
    }).then(res => {
      console.log(res)
      this.data = res.items
      this.pagination.currentPage = res._meta.page
      this.pagination.pageSize = res._meta.per_page
      this.pagination.total = res._meta.total_items
      console.log(...this.pagination)
    })
  },
  methods: {
    paginationCurrentChange (currentPage) {
      this.pagination.currentPage = currentPage
      this.fetchData()
    },
    fetchData () {
      this.loading = true
      request({
        url: '/schools',
        method: 'get',
        ...this.pagination
      }).then(res => {
        this.data = res.items
        this.pagination.currentPage = res._meta.page
        this.pagination.pageSize = res._meta.per_page
        this.pagination.total = res._meta.total_items
        this.loading = false
      }).catch(err => {
        console.log('err', err)
        this.loading = false
      })
    }
  }

}
</script>
