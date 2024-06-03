<template>
  <div class="signup-form">
    <form @submit.prevent="sign(signdata)" class='account-info'>
      <p><input v-model.trim="signdata.name" @input="limitNickname" type="text" placeholder="name" class="input-prop"></p>
      <p><input v-model.trim="signdata.username" @input="limitPassword"  placeholder="username" class="input-prop"></p>
      <p><input v-model.trim="signdata.password" type="password" placeholder="password" class="input-prop"></p>
      <button class="signup-btn">Sign Up</button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useStore } from '@/stores/dev_test';

export default {
  setup() {
    const account = ref(useStore());
    const signdata = {
      name: '',
      username: '',
      password: ''
    }
    
    const sign = (data) => {
      account.value.signup(data)
    }
    return {
      signdata,
      sign
    }
  },
}
</script>

<style scoped>
.signup-form{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 40vh;
}
input {
  font-size: 15px;
  margin-bottom: 5px;
  border-radius: 5px;
  width: 25vh;
  height: 4vh;
  margin: 0px 5px;
  background-color: azure;
}
</style>
