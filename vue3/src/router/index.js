import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Login',
      component: () => import('@/views/Login.vue')
    },
    {
      path: '/ping',
      name: 'Ping',
      component: () => import('@/views/Ping.vue')
    },
    {
      path: '/pong',
      name: 'Pong',
      component: () => import('@/views/Pong.vue')
    },
    {
      path: '/books',
      name: 'Books',
      component: () => import('@/views/Books.vue')
    }
  ]
})

export default router
