import { createRouter, createWebHashHistory } from 'vue-router'
import PanelList from '@/views/admin/panel/PanelList'

const routes = [
  {
    path: '/',
    name: 'PanelList',
    component: PanelList
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
