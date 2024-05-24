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
  </div>
</template>

<script>
import { ref } from 'vue';
import BoardListView from '@/components/BoardListView.vue'
import { useStore } from '@/stores/dev_test';
export default {
  components: {
    BoardListView
  },
  setup() {
    const boards = ref(useStore())
    boards.value.fatchBoards()
    return {
      boards
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
}
.boardlist {
  justify-content: center;
  align-items: center;
  width: 100vw;
  height: 8vh;
  margin: 5vw;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
table {
  width : 300px;
  height : 200px;
}
th, td {
  text-align: center;
}
</style>
