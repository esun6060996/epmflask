// 菜单 侧边栏
export default [
  { path: '/index', title: '首页', icon: 'home' },
  {
    title: '基础数据',
    icon: 'folder-o',
    children: [
      { path: '/org', title: '组织架构' },
      { path: '/school', title: '学校管理' },
      { path: '/user', title: '用户管理' }
    ]
  },
  {
    title: '测试应用',
    icon: 'folder-o',
    children: [
      { path: '/chart', title: '图表' },
      { path: '/label', title: '标签' },
      { path: '/test', title: '测试' }
    ]
  }
]
