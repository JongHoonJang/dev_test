import { createRouter, createWebHistory } from "vue-router";
import BoardCreateView from "@/components/BoardCreateView";
import BoardDetailView from "@/components/BoardDetailView";
import BoardListView from "@/components/BoardListView";
import CommentCreateView from "@/components/BoardEditView";
import MainView from "@/components/MainView";


const routes = [
  {
    path: "/",
    name: "MainView",
    component: MainView
  },
  {
    path: "/board",
    name: "BoardListView",
    component: BoardListView
  },
  {
    path: "/board/create",
    name: "BoardCreateView",
    component: BoardCreateView
  },
  {
    path: "/board/:board_id",
    name: "BoardDetailView",
    component: BoardDetailView
  },
  {
    path: "/board/:board_id/edit",
    name: "BoardEditView",
    component: CommentCreateView
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});
// 로우터 가드
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("token")
  // 글쓰기페이지에서 토큰이 존재하지 않으면 로그인화면으로 이동
  if (to.name === "BoardCreateView") {
    if(!token) {
      next({ name:"MainView" });
    }
  }
  // 글수정페이지에서 토큰이 존재하지 않으면 로그인화면으로 이동
  else if (to.name === "BoardEditView") {
    if(!token) {
      next({ name:"MainView" });
    }
  }

  next();
});
export default router;
