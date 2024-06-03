<template>
  <div id="board-write">
      <div id="write-area">
        <form @submit.prevent="boardUpdate(credentials)" enctype="multipart/form-data" method="post">
          <div class="box">제목</div>
          <div id="in-title">
            <input v-model.trim="credentials.title" name="title" id="utitle" rows="1" cols="55" placeholder="제목" maxlength="100" required>
          </div>

          <div class="box">내용</div>
            <div id="in-content">
              <textarea v-model.trim="credentials.content" name="content" id="ucontent" placeholder="내용" required></textarea>
            </div>
            
            <div class="bt-se">
              <button type="submit">글 수정</button>
              <div>
                <router-link class="button" :to="{ name: 'BoardDetailView', params:{board_id: board_id}}">취소</router-link>
              </div>
            </div>
          </form>
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

<style scoped>
.board-write{
  display: flex;
}
.button {
  border: 2px solid black;
}
.button, button{
  margin: 5px;
  background-color:#4CAF50;
  color:white;
  font-size:15px;
  padding: 5px 10px;
  border-radius : 5px;
}
.button:hover, button:hover{

 cursor:pointer;
 opacity:0.8;
}
input, textarea {
  font-size: 18px;
  margin-bottom: 5px;
  border-radius: 5px;
  width: 80vh;
}
textarea {
  height: 20vh;
}
input {
  height: 5vh;
}
.box{
  background-color: aquamarine;
  margin: 10px 0px;
  font-size: 18px;
  padding: 5px 10px;
  border-radius : 5px;
  border: 1px solid black;
}

.bt-se{
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>