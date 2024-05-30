<template>
  <div class='Page'>
    <table class="boardlist">
      <thead>
        <tr style="background-color: #ccffee">
          <th>번호</th>
          <th class="title">제목</th>
          <th>작성자</th>
          <th>작성일</th>
          <th>조회</th>
        </tr>
      </thead>
      <tbody>
        <BoardListView
        v-for="board in boards.boards"
        :key="board.id"
        :board="board"
        />
      </tbody>
    </table>
    <div >
        <button class='create_board' @click="writing()">글쓰기</button>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import router from '@/router';
import BoardListView from '@/components/BoardListView.vue'
import { useStore } from '@/stores/dev_test';
export default {
  components: {
    BoardListView
  },
  setup() {
    const boards = ref(useStore())
    boards.value.fatchBoards()
    const writing = () => {
      router.push({name: 'BoardCreateView'})
    }
    return {
      boards,
      writing
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.Nav {
  display: flex;
  justify-content: space-between;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  text-decoration-line: none;
  
}
.Page {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100vw;
  height: 8vh;
  flex-direction: column;
}
.boardlist {
  justify-content: center;
  align-items: center;
  width: 70vw;
  height: 8vh;
  margin: 5vw;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
tr {
  height: 4vh;
}
table {
  width : 300px;
  height : 200px;
}
th {
  text-align: center;
}
.create_board{
  background-color: #ccffee;
}

</style>
