import { createRouter, createWebHistory } from 'vue-router'

import AboutView from '../views/AboutView.vue'
import CommentsView from '../views/CommentsView.vue'
import HomeView from '../views/HomeView.vue'
import PlayersView from '../views/PlayersView.vue'
import TeamsView from '../views/TeamsView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/players',
    name: 'players',
    component: PlayersView,
  },
  {
    path: '/teams',
    name: 'teams',
    component: TeamsView,
  },
  {
    path: '/comments',
    name: 'comments',
    component: CommentsView,
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
