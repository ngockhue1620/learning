import Vue from 'vue'
import VueRouter from 'vue-router'

import Exam from '../components/question'


Vue.use(VueRouter)
const routes = [
  {
    path: '/exam',
    component: Exam,
    children: [
      // {
      //   path: '/cart',
      //   component: Cart,
      //   meta: { requireAuth: true }
      // }
    ]
  },
]
const router = new VueRouter({
  routes
})
export default router;