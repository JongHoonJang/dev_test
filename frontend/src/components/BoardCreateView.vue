<template>
  <div id="board-write">
      <div id="write-area">
        <form @submit.prevent="boardCreate(credentials)" enctype="multipart/form-data" method="post">
          <div class="box">제목</div>
          <div id="in-title">
            <input v-model.trim="credentials.title" name="title" id="utitle" rows="1" cols="55" placeholder="제목" maxlength="100" required>
          </div>

          <div class="box">내용</div>
            <div id="in-content">
              <textarea v-model.trim="credentials.content" name="content" id="ucontent" placeholder="내용" required></textarea>
            </div>
            
            <div class="bt-se">
              <button type="submit">글 작성</button>
              <div >
                <a class="button" v-if="answer" @click="close()" id="close">댓글취소</a>
                <a class="button" v-if="!answer" @click="goMain()">취소</a>
              </div>
            </div>
          </form>
          
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
    const goMain = () => {
      router.push({ name: 'MainView' })
    }
    return {
      credentials,
      boardCreate,
      answer,
      close,
      goMain
    };
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
  width: 70vh;
}
textarea {
  height: 15vh;
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