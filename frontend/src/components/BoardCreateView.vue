<template>
  <div id="board_write">
    <h4>글을 작성하는 공간입니다.</h4>
      <div id="write_area">
        <form @submit.prevent="boardCreate(credentials)" enctype="multipart/form-data" method="post">
          <div id="in_title">
            <textarea v-model.trim="credentials.title" name="title" id="utitle" rows="1" cols="55" placeholder="제목" maxlength="100" required></textarea>
          </div>
 
          <div class="wi_line"></div>
            <div id="in_content">
              <textarea v-model.trim="credentials.content" name="content" id="ucontent" placeholder="내용" required></textarea>
            </div>
 
            <div class="bt_se">
              <button type="submit">글 작성</button>
            </div>
            <div>
              <router-link :to="{ name: 'MainView' }">취소</router-link>
            </div>
          </form>
        </div>
  </div>      
</template>

<script>
import { ref } from 'vue';
// import router from '@/router';
import { useStore } from '@/stores/dev_test';

export default {
  setup() {
    const dev_test = ref(useStore());
    const credentials = {
      title: '',
      content: ''
    }
    const boardCreate = (data) => {
      dev_test.value.createBoard(data)
    }
    return {
      credentials,
      boardCreate
    };
  }
};
</script>