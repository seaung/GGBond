import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '../store/user'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: () => import('../views/login/index.vue'),
      meta: {
        title: '登录',
        requiresAuth: false
      }
    },
    {
      path: '/',
      component: () => import('../layout/index.vue'),
      redirect: '/dashboard',
      children: [
        {
          path: 'dashboard',
          name: 'Dashboard',
          component: () => import('../views/dashboard/index.vue'),
          meta: {
            title: '仪表盘',
            requiresAuth: true
          }
        },
        {
          path: 'devices',
          name: 'Devices',
          component: () => import('../views/devices/index.vue'),
          meta: {
            title: '设备管理',
            requiresAuth: true
          }
        },
        {
          path: 'vulnerabilities',
          name: 'Vulnerabilities',
          component: () => import('../views/vulnerabilities/index.vue'),
          meta: {
            title: '漏洞扫描',
            requiresAuth: true
          }
        },
        {
          path: 'tasks',
          name: 'Tasks',
          component: () => import('../views/tasks/index.vue'),
          meta: {
            title: '任务管理',
            requiresAuth: true
          }
        }
      ]
    }
  ]
})

// 全局前置守卫
// router.beforeEach((to, from, next) => {
//   const userStore = useUserStore()
//   const token = userStore.token || localStorage.getItem('token')

//   // 设置页面标题
//   document.title = `${to.meta.title || 'GGBond'}`

//   // 判断该路由是否需要登录权限
//   if (to.meta.requiresAuth) {
//     if (token) {
//       next()
//     } else {
//       next({
//         path: '/login',
//         query: { redirect: to.fullPath }
//       })
//     }
//   } else {
//     if (token && to.path === '/login') {
//       // 已登录且要跳转的页面是登录页
//       next({ path: '/' })
//     } else {
//       next()
//     }
//   }
// })

export default router