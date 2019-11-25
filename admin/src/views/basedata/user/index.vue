<template>
    <d2-container>
        <template slot="header">
            Page 2 Get:api/Users
        </template>
            <d2-crud
            ref="d2Crud"
            :columns="columns"
            :data="data"
            :options="options"/>
    </d2-container>
</template>

<script>
import request from '@/plugin/axios'
export default {
  data() {
    return {
            columns:[
                {
                title: '姓名',
                key: 'userName',
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
                title: '微信',
                key: 'wexin'
                },
                {
                title: 'QQ',
                key: 'qq'
                }
            ],
            data:{},
            options: {
                border: true,
                stripe: true,
                height: '600'
            }
        }
    },
    name: 'user',
    created() {
        request({
            url: '/users',
            method: 'get'
        }).then(res => {
            console.log(typeof(res));
            this.data= res;
            
            console.log(this.data);
        });
    }
}
</script>
