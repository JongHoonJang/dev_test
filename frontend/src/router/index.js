import { createRouter, createWebHistory } from 'vue-router'
import BoardCreateView from '@/components/BoardCreateView.vue'
import BoardDetailView from '@/components/BoardDetailView.vue'
import BoardListView from '@/components/BoardListView.vue'
import CommentCreateView from '@/components/CommentCreateView.vue'
import CommentListView from '@/components/CommentListView.vue'
import MainView from '@/components/MainView.vue'


const routes = [
  {
    path: '/',
    name: 'MainView',
    component: MainView
  },
  {
    path: '/board',
    name: 'BoardListView',
    component: BoardListView
  },
  {
    path: '/board/create',
    name: 'BoardCreateView',
    component: BoardCreateView
  },
  {
    path: '/board/:board_id',
    name: 'BoardDetailView',
    component: BoardDetailView
  },
  {
    path: '/board/:board_id/comment',
    name: 'CommentListView',
    component: CommentListView
  },
  {
    path: '/board/:board_id/comment/create',
    name: 'CommentCreateView',
    component: CommentCreateView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
