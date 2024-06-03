import { defineStore } from "pinia";
import axios from "axios";
import router from "@/router";
import api from "@/api/api";
import Swal from "sweetalert2";

export const useStore = defineStore("dev_test", {
  state: () => ({
    accesstoken: localStorage.getItem("token") || "",
    boards: [],
    board: {},
  }),
  getters: {
    isLoggedIn: (state) => !!state.accesstoken,
    authHeader: (state) => ({ Authorization: `Bearer ${state.accesstoken}` }),
  },
  actions: {
    addCounting(board_id) {
      axios
        .post(api.boards.boards_counting(board_id),{}, {
          headers: this.authHeader,
        })
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.error(err.response);
        });
    },
    fatchBoards() {
      axios
        .get(api.boards.boards_list(), {
        })
        .then((res) => {
          this.boards = res.data;
        })
        .catch((err) => {
          console.error(err.response);
        });
    },
    fatchBoard(data) {
      axios
        .get(api.boards.boards_detail_update_delete(data), {
        })
        .then((res) => {
          this.board = res.data;
        })
        .catch((err) => {
          console.error(err.response);
        });
    },
    createBoard(data) {
      axios
        .post(api.boards.boards_create(), {
          no: data.no,
          data: {
            title: data.title,
            content: data.content
          },
        },{headers: this.authHeader})
        .then((res) => {
          Swal.fire({
            title: "dev_test",
            text: "게시글이 작성되었습니다.",
            icon: "success",
          });
          this.boards = res.data;
          this.reissueToken()
          router.push({ name: "MainView" });
        })
        .catch((err) => {
          console.error(err.response);
        });
    },
    updateBoard(data) {
      axios
        .put(api.boards.boards_detail_update_delete(data.no), {
          data: {
            title: data.title,
            content: data.content
          },
        },{headers: this.authHeader})
        .then((res) => {
          Swal.fire({
            title: "dev_test",
            text: "게시글이 수정되었습니다.",
            icon: "success",
          });
          this.boards = res.data;
          this.reissueToken()
          router.push({ name: "BoardDetailView" });
        })
        .catch((err) => {
          console.error(err.response);
        });
    },
    deleteBoard(data) {
      axios
        .delete(api.boards.boards_detail_update_delete(data),{
          headers: this.authHeader,
        })
        .then((res) => {
          Swal.fire({
            title: "dev_test",
            text: "게시글이 삭제되었습니다.",
            icon: "success",
          });
          this.boards = res.data;
          router.push({ name: "MainView" });
        })
        .catch((err) => {
          Swal.fire({
            title: "dev_test",
            text: err.data,
            icon: "error",
          });
        });
    },
    reissueToken() {
      const refresh = localStorage.getItem('refresh')
      axios
        .post(api.accounts.reissue(), {
          refresh: refresh
        })
        .then((res) => {
          this.saveToken(res.data.access);
        })
        .catch(() => {
          Swal.fire({
            title: "CURI@US",
            text: "인증에 실패하였습니다..",
            icon: "error",
          });
          this.removeToken();
        });
    },
    saveToken(token) {
      this.accesstoken = token;
      localStorage.setItem("token", token);
    },
    //token값 삭제
    removeToken() {
      this.accesstoken = "";
      localStorage.setItem("token", "");
      localStorage.removeItem("refresh")
    },
    signup(data) {
      axios
      .post(api.accounts.signup(), {
        data: data
      })
      .then(() => {
        Swal.fire({
          title: "dev_test",
          text: "회원가입되었습니다.",
          icon: "success",
        });
        setTimeout(() => router.go(0), 3000);
      })
      .catch(() => {
        Swal.fire({
          title: "dev_test",
          text: "인증에 실패하였습니다..",
          icon: "error",
        });
        this.removeToken();
      });
    },
    fetchLogin(credentials) {
      axios
        .post(api.accounts.login(), {
          data: {
            username: credentials.username,
            password: credentials.password
          },
        })
        .then((res) => {
          Swal.fire({
            title: "dev_test",
            text: "로그인 되었습니다.",
            icon: "success",
          });
          this.saveToken(res.data.access);
          localStorage.setItem("refresh", res.data.refresh)
          router.push({ name: "MainView" });
        })
        .catch((err) => {
          console.error(err.response);
        });
    },
    logout() {
      axios
        .post(api.accounts.logout(),{}, {
          headers: this.authHeader,
        })
        .then(() => {
          this.removeToken();
          Swal.fire({
            title: "dev_test",
            text: "로그아웃 되었습니다.",
            icon: "success",
          });
          router.push({ name: "MainView" });
        })
        .catch(() => {
          this.reissueToken()
          this.logout()
        })
    },
    fetchProfile() {
      axios
        .get(api.accounts.profile(), {
          headers: this.authHeader,
        })
        .then((res) => {
          this.profile = res.data.data;
        })
        .catch((error) => {
          if (error.response.status == 401) {
            axios
              .get(api.accounts.reissue(), {
                withCredentials: true,
              })
              .then((res) => {
                this.saveToken(res.data.data);
                this.fetchProfile();
              })
              .catch(() => {
                Swal.fire({
                  title: "CURI@US",
                  text: "인증에 실패하였습니다..",
                  icon: "error",
                });
                this.removeToken();
              });
          }
        });
    },
    userDelete() {
      axios
        .delete(api.accounts.delete(), {
          headers: this.authHeader,
        })
        .then(() => {
          Swal.fire({
            title: "CURI@US",
            text: "회원탈퇴 되었습니다.",
            icon: "success",
          });
          this.removeToken();
          router.push({ name: "RandingView" });
        })
        .catch((error) => {
          if (error.response.status == 401) {
            axios
              .get(api.accounts.reissue(), {
                withCredentials: true,
              })
              .then((res) => {
                this.saveToken(res.data.data);
                this.userDelete();
              })
              .catch(() => {
                Swal.fire({
                  title: "CURI@US",
                  text: "인증에 실패하였습니다..",
                  icon: "error",
                });
                this.removeToken();
              });
          }
        });
    },
  },
});
