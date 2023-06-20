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
      path: '/books',
      name: 'Books',
      component: () => import('@/views/Books.vue')
    }
  ]
})

export default router
