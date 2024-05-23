<template>
    <nav class="nav-bar">
      <div class="nav-bar-login">
        <div class="nav-laft">
          <a v-if="account.isLoggedIn" @click="logout()">로그아웃</a>
        </div>
        <form v-if="!account.isLoggedIn" @submit.prevent="login(credentials)" class='account-info'>
          <p><input v-model.trim="credentials.username" type="username" placeholder="username" class="input-prop"></p>
          <p><input v-model.trim="credentials.password" type="password" placeholder="password" class="input-prop"></p>
            <div class="btn-box">
              <button class="login-btn">Sign In</button>
          </div>
        </form>
      </div>
      <div>
        <a class='create_board' @click="writing()">글쓰기</a>
      </div>
    </nav>
</template>

<script>
import { ref } from 'vue';
import { useStore } from '@/stores/dev_test';
import router from '@/router';
import Swal from 'sweetalert2';
export default {
  setup() {
    const account = ref(useStore());
    const credentials = {
      username: '',
      password: ''
    }
    const writing = () => {
      router.push({name: 'BoardCreateView'})
    }
    const login = (data) => {
      account.value.fetchLogin(data)
    };
    const logout = () => {
      Swal.fire({
        title: 'CURI@US',
        text: '로그아웃 하시겠습니까?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes",
      }).then((result) => {
        if (result.isConfirmed) {
          account.value.logout();
        }
      });
    };
    return {
      account,
      credentials,
      login,
      logout,
      writing,
    };
  },
};
</script>

<style scoped>
/* @font-face {
  font-family: "BMJUA_ttf";
  src: url(../assets/BMJUA_ttf.ttf);
  font-weight: normal;
  font-style: normal;
} */
nav {
  margin: 0;
  width: 99vw;
}
.nav-bar {
  padding: 8px 12px;
  background-color: aqua;
  position: fixed;
  top: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 6vh;
  margin: 0;
  z-index: 1;
}

/* .nav-bar-login {
  font-family: "BMJUA_ttf";
  border-style: none;
  background: none;
  margin-right: 5vw;
} */

.nav-laft {
  display: flex;
}

.nav-laft a {
  margin: 5px;
  text-decoration: none;
  color: black;
}
.nav-laft a:hover {
  color: gold;
}
</style>
