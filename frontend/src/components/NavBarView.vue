<template>
    <nav class="nav-bar">
      <div class="nav-bar-login">
        <div class="nav-laft">
          <a v-if="account.isLoggedIn" @click="logout()">로그아웃</a>
        </div>
        <form v-if="!account.isLoggedIn" @submit.prevent="login(credentials)" class='account-info'>
          <div>
            <input v-model.trim="credentials.username" type="username" placeholder="username" class="input-prop">
            <input v-model.trim="credentials.password" type="password" placeholder="password" class="input-prop">
            <div class="btn-box">
              <button class="login-btn">Sign In</button>
            </div>
          </div>
        </form>
      </div>
      <div v-if="!account.isLoggedIn" class="signup" @click="isModalViewed=true">회원가입</div>
    </nav>
    <ModalView v-if="isModalViewed" @close-modal="isModalViewed=false">
        <SignupView/>
    </ModalView>
</template>

<script>
import { ref } from 'vue';
import { useStore } from '@/stores/dev_test';
import Swal from 'sweetalert2';
import ModalView from '@/components/ModalView.vue';
import SignupView from '@/components/SignupView.vue';
export default {
  components: {
    SignupView,
    ModalView,
  },
  data() {
    return {
      isModalViewed: false,
    }
  },
  setup() {
    const account = ref(useStore());
    const credentials = {
      username: '',
      password: ''
    }
    const login = (data) => {
      account.value.fetchLogin(data)
    };
    const logout = () => {
      Swal.fire({
        title: 'dev_test',
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

.nav-bar-login .account-info {
  align-items: center;
  border-style: none;
  background: none;
  margin-right: 5vw;
}

.nav-laft {
  display: flex;
}

.nav-laft a {
  margin: 5px;
  text-decoration: none;
  color: black;
}
.nav-laft a:hover {
  color: blue;
}
.signup {
  margin-right: 10px;
}
.signup:hover{
  color: blue;
}
input {
  font-size: 15px;
  margin-bottom: 5px;
  border-radius: 5px;
  width: 10vh;
  margin: 0px 5px;
}
button{
  margin: 5px 5px;
  background-color:#4CAF50;
  color:white;
  font-size:13px;
  padding: 5px 10px;
  border-radius : 5px;
}
button:hover{

 cursor:pointer;
 opacity:0.8;
}
</style>
