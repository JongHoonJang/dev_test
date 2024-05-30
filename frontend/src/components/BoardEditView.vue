<template>
  <div id="board_write">
      <div id="write_area">
        <form @submit.prevent="boardUpdate(credentials)" enctype="multipart/form-data" method="post">
          <div>제목</div>
          <div id="in_title">
            <textarea v-model.trim="credentials.title" name="title" id="utitle" rows="1" cols="55" placeholder="제목" maxlength="100" required></textarea>
          </div>

          <div class="wi_line">내용</div>
            <div id="in_content">
              <textarea v-model.trim="credentials.content" name="content" id="ucontent" placeholder="내용" required></textarea>
            </div>
            
            <div class="bt_se">
              <button type="submit">글 수정</button>
            </div>
          </form>
          <div>
              <!-- <button v-if="answer" @click="close()" id="close">댓글취소</button> -->
              <router-link  :to="{ name: 'MainView' }">취소</router-link>
          </div>
        </div>
  </div>
</template>

<script>
import { ref } from 'vue';
// import router from '@/router';
import { useStore } from '@/stores/dev_test';
import { useRoute } from 'vue-router'
export default {
  setup(){
    const route = ref(useRoute())
    const board_id = ref(route.value.params.board_id)
    const boards = ref(useStore())
    boards.value.fatchBoard(board_id.value)
    const credentials = {
      no: board_id.value,
      title: boards.value.board.title,
      content: boards.value.board.content
    }
    const boardUpdate = (data) => {
      boards.value.updateBoard(data)
    }
    return {
      credentials,
      boardUpdate
    }
  }
};
</script>