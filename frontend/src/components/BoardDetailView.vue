<template>
  <div class="board-detail">
    <div class="board-q">
      <div class="list-box">유형</div>
      <div class="q-box" v-if="!isQuestion">
        질문
      </div>
      <div class="q-box" v-if="isQuestion">
        답변
      </div>
    </div>
    <div class="title-box">제목</div>
    <div class="t-box">
      {{boards.board.title}}
    </div>
    <div class="content-box">내용</div>
    <div class="c-box">
      {{boards.board.content}}
    </div>
    <div class="buttons">
      <button v-if="boards.isLoggedIn" @click="isAnswer=true">답변</button>
      <button v-if="boards.isLoggedIn" @click="deleteBoard()">삭제</button>
      <button v-if="boards.isLoggedIn" @click="editBoard()">수정</button>
      <button @click="back()">닫기</button>
    </div>
    <BoardCreateViewVue v-if="isAnswer"
    :isAnswer="isAnswer"
    :board_id="board_id"
    />
  </div>
</template>

<script>
import { ref } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "@/stores/dev_test";
import router from "@/router";
import BoardCreateViewVue from "@/components/BoardCreateView";
import Swal from "sweetalert2";
export default {
  components:{
    BoardCreateViewVue
  },
  data(){
    return {
      isAnswer:false
    };
  },
  setup () {
    const route = ref(useRoute());
    const board_id = ref(route.value.params.board_id);
    const boards = ref(useStore());
    boards.value.fatchBoard(board_id.value);
    const isQuestion = !!boards.value.board.order_id;
    const back = () => {
      router.push({ name:"MainView"})
    };
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
    };
    const editBoard = () => {
      if (boards.value.isLoggedIn){
        router.push({ name: "BoardEditView",params: {board_id: board_id.value} });
      }
      else{
        Swal.fire({
            title: "dev_test",
            text: "로그인을 해주세요.",
            icon: "error",
          });
      }
    };
    return {
      boards,
      board_id,
      isQuestion,
      back,
      deleteBoard,
      editBoard
    };
  }
};
</script>

<style scoped>
.board-detail{
  flex-direction: column;
  justify-self: center;
  align-items: center;
  margin-top: 30px;
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
.q-box ,.list-box{
  margin: 5px 0px;
  font-size:18px;
  padding: 5px 10px;
  border-radius : 5px;
  border: 1px solid black;
  font-weight: bolder;
  width: 10vh;
  text-align: center;
}
.q-box {
  margin-right: 46.5vh;
}
.list-box{
  background-color: aquamarine;
}
.board-q{
  display: flex;
}
.title-box, .t-box{
  margin: 5px 0px;
  font-size:18px;
  padding: 5px 10px;
  border-radius : 5px;
  border: 1px solid black;
  width: 69vh
}
.title-box {
  background-color: aquamarine;
  font-weight: bolder;
}
.c-box, .content-box {
  margin: 5px 0px;
  font-size:18px;
  padding: 5px 10px;
  border-radius : 5px;
  border: 1px solid black;
  width: 69vh
}
.content-box {
  background-color: aquamarine;
  font-weight: bolder;
}
.c-box {
  height: 15vh;
}
</style>