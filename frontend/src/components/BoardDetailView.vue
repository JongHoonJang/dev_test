<template>
  <div class="board-detail">
    <div>유형</div>
    <div>
      {{board_data.id}}
    </div>
    <div>제목</div>
    <div>
      {{board_data.title}}
    </div>
    <div>내용</div>
    <div>
      {{board_data.content}}
    </div>
    <div>댓글</div>
    <div>
      {{board_data.comment_set}}
    </div>
    <button>답변</button>
    <button>삭제</button>
    <button>수정</button>
    <button>닫기</button>
  </div>
</template>

<script>
import { ref } from "vue"
import { useRoute } from 'vue-router'
import { useStore } from '@/stores/dev_test';
export default {
  setup () {
    const route = useRoute()
    const board_id = ref(route.params.board_id)
    const boards = ref(useStore())
    boards.value.fatchBoard(board_id.value)
    const board_data = boards.value.board
    return {
      board_data
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
</style>