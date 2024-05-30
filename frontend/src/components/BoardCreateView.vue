<template>
  <div id="board_write">
      <div id="write_area">
        <form @submit.prevent="boardCreate(credentials)" enctype="multipart/form-data" method="post">
          <div>제목</div>
          <div id="in_title">
            <textarea v-model.trim="credentials.title" name="title" id="utitle" rows="1" cols="55" placeholder="제목" maxlength="100" required></textarea>
          </div>

          <div class="wi_line">내용</div>
            <div id="in_content">
              <textarea v-model.trim="credentials.content" name="content" id="ucontent" placeholder="내용" required></textarea>
            </div>
            
            <div class="bt_se">
              <button type="submit">글 작성</button>
            </div>
          </form>
          <div>
              <button v-if="answer" @click="close()" id="close">댓글취소</button>
              <router-link v-if="!answer" :to="{ name: 'MainView' }">취소</router-link>
          </div>
        </div>
  </div>      
</template>

<script>
import { ref } from 'vue';
import router from '@/router';
import { useStore } from '@/stores/dev_test';

export default {
  props:['isAnswer','board_id'],
  setup(props) {
    const dev_test = ref(useStore());
    const ans = ref(props)
    const answer = ans.value.isAnswer
    const credentials = {
      no: -1,
      title: '',
      content: ''
    }
    const close = () => {
      router.go(0)
    }
    const boardCreate = (data) => {
      if (ans.value.board_id) {
        data.no = ans.value.board_id
      }
      console.log(data)
      dev_test.value.createBoard(data)
    }
    return {
      credentials,
      boardCreate,
      answer,
      close
    };
  }
};
</script>

<style scoped>
.board_write{
  display: flex;
}
</style>