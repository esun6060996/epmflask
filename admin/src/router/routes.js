import layoutHeaderAside from '@/layout/header-aside'

// 由于懒加载页面太多的话会造成webpack热更新太慢，所以开发环境不使用懒加载，只有生产环境使用懒加载
const _import = require('@/libs/util.import.' + process.env.NODE_ENV)

/**
 * 在主框架内显示
 */
const frameIn = [
  {
    path: '/',
    redirect: { name: 'index' },
    component: layoutHeaderAside,
    children: [
      // 首页
      {
        path: 'index',
        name: 'index',
        meta: {
          auth: true
        },
        component: _import('system/index')
      },
      // 应用页面
      {
        path: 'org',
        name: 'org',
        meta: {
          title: '组织架构',
          auth: true
        },
        component: _import('basedata/org')
      },
      {
        path: 'school',
        name: 'school',
        meta: {
          title: '学校管理',
          auth: true
        },
        component: _import('basedata/school')
      },
      {
        path: 'user',
        name: 'user',
        meta: {
          title: '用户管理',
          auth: true
        },
        component: _import('basedata/user')
      },
      // 做一些测试用
      {
        path: 'chart',
        name: 'chaet',
        meta: {
          title: '图表',
          auth: true
        },
        component: _import('test/chart')
      },
      {
        path: 'label',
        name: 'label',
        meta: {
          title: '标签',
          auth: true
        },
        component: _import('test/label')
      },
      {
        path: 'test',
        name: 'test',
        meta: {
          title: '测试',
          auth: true
        },
        component: _import('test/test')
      },
      // 系统 前端日志
      {
        path: 'log',
        name: 'log',
        meta: {
          title: '前端日志',
          auth: true
        },
        component: _import('system/log')
      },
      // 刷新页面 必须保留
      {
        path: 'refresh',
        name: 'refresh',
        hidden: true,
        component: _import('system/function/refresh')
      },
      // 页面重定向 必须保留
      {
        path: 'redirect/:route*',
        name: 'redirect',
        hidden: true,
        component: _import('system/function/redirect')
      }
    ]
  }
]

/**
 * 在主框架之外显示
 */
const frameOut = [
  // 登录
  {
    path: '/login',
    name: 'login',
    component: _import('system/login')
  }
]

/**
 * 错误页面
 */
const errorPage = [
  {
    path: '*',
    name: '404',
    component: _import('system/error/404')
  }
]

// 导出需要显示菜单的
export const frameInRoutes = frameIn

// 重新组织后导出
export default [
  ...frameIn,
  ...frameOut,
  ...errorPage
]
