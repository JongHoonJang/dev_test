import { defineStore } from "pinia";
import axios from "axios";
import router from "@/router";
import api from "@/api/api";
import Swal from "sweetalert2";

export const useStore = defineStore("dev_test", {
  state: () => ({
    accesstoken: localStorage.getItem("token") || "",
    boards: [],
  }),
  getters: {
    isLoggedIn: (state) => !!state.accesstoken,
    authHeader: (state) => ({ Authorization: `Bearer ${state.accesstoken}` }),
  },
  actions: {
    fatchBoard() {
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
    createBoard(data) {
      axios
        .post(api.boards.boards_create(), {
          params: {
            title: data.title,
            content: data.content
          },
          headers: {
            "Access-Control-Allow-Origin": "*",
          },
        })
        .then((res) => {
          Swal.fire({
            title: "dev_test",
            text: "게시글이 작성되었습니다.",
            icon: "success",
          });
          this.saveToken(res.data.data);
          router.push({ name: "MainView" });
        })
        .catch((err) => {
          console.error(err.response);
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
    },
    fetchLogin(type, code) {
      axios
        .get(api.accounts.login(type), {
          params: {
            code: code,
          },
          headers: {
            "Access-Control-Allow-Origin": "*",
          },
        })
        .then((res) => {
          Swal.fire({
            title: "dev_test",
            text: "로그인 되었습니다.",
            icon: "success",
          });
          this.saveToken(res.data.data);
          router.push({ name: "MainView2" });
        })
        .catch((err) => {
          console.error(err.response);
        });
    },
    logout() {
      axios
        .get(api.accounts.logout(), {
          withCredentials: true,
        })
        .then(() => {
          this.removeToken();
          Swal.fire({
            title: "dev_test",
            text: "로그아웃 되었습니다.",
            icon: "success",
          });
          router.push({ name: "RandingView" });
        });
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
    tokenReissue() {
      axios
        .get(api.accounts.reissue(), {
          withCredentials: true,
          headers: this.authHeader,
        })
        .then((res) => {
          this.saveToken(res.data.data);
        })
        .catch(() => {
          this.logout();
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
