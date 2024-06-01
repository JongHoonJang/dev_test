<template>
  <div class="board-detail">
    <div>유형</div>
    <div v-if="!isQuestion">
      질문
    </div>
    <div v-if="isQuestion">
      답변
    </div>
    <div>제목</div>
    <div>
      {{boards.board.title}}
    </div>
    <div>내용</div>
    <div>
      {{boards.board.content}}
    </div>
    <div class="buttons">
      <button @click="isAnswer=true">답변</button>
      <button @click="deleteBoard()">삭제</button>
      <button @click="editBoard()">수정</button>
      <button @click="back()">닫기</button>
    </div>
    <BoardCreateViewVue v-if="isAnswer"
    :isAnswer="isAnswer"
    :board_id="board_id"
    />
  </div>
</template>

<script>
import { ref } from "vue"
import { useRoute } from 'vue-router'
import { useStore } from '@/stores/dev_test';
import router from '@/router';
import BoardCreateViewVue from '@/components/BoardCreateView.vue';
import Swal from "sweetalert2";
export default {
  components:{
    BoardCreateViewVue
  },
  data(){
    return {
      isAnswer:false
    }
  },
  setup () {
    const route = ref(useRoute())
    const board_id = ref(route.value.params.board_id)
    const boards = ref(useStore())
    boards.value.fatchBoard(board_id.value)
    const isQuestion = !!boards.value.board.order_id
    const back = () => {
      router.push({ name:"MainView"})
    }
    const deleteBoard = () =>{
      if (boards.value.isLoggedIn){
        boards.value.deleteBoard(board_id.value)
      }
      else{
        Swal.fire({
            title: "dev_test",
            text: "로그인을 해주세요.",
            icon: "error",
          });
      }
    }
    const editBoard = () => {
      router.push({ name: 'BoardEditView',params: {board_id: board_id.value} })
    }
    return {
      boards,
      board_id,
      isQuestion,
      back,
      deleteBoard,
      editBoard
    }
  }
};
</script>

<style scoped>
.board-detail{
  flex-direction: column;
  justify-self: center;
  align-items: center;
}
.buttons{
  flex-direction: column;
}
button{
  margin: 5px;
  background-color:#4CAF50;
  color:white;
  font-size:15px;
  padding: 5px 10px;
  border-radius : 5px;
}
button:hover{

 cursor:pointer;
 opacity:0.8;
}
</style>