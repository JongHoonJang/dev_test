<template>
	<tr>
		<td class='td' v-if="!isQuestion" >Q</td>
    <td class='td' v-if="isQuestion" >A</td>
		<td>
		<c:choose>
		<c:otherwise>
      <pre v-if="!boards.board.depth" @click="to_detail()">{{boards.board.title}}</pre>
			<pre v-if="boards.board.depth" @click="to_detail()">{{blank}} {{boards.board.title}}</pre>
		</c:otherwise>
		</c:choose>					
		</td>
		<td class='td'>{{boards.board.user_id.name}}</td>
		<td class='td'>{{day}} {{time[0]}}</td>
		<td class='td'>{{boards.board.board_counting}}</td>
	</tr>
</template>

<script>
import { ref } from 'vue';
import router from "@/router";
import { useStore } from '@/stores/dev_test';
export default {
  props: ['board'],
  setup(props) {
    const api = useStore()
    const boards = ref(props)
    const board_id = ref(boards.value.board.id)
    const timedata = (boards.value.board.created_at).split('T')
    const day = timedata[0]
    const time = timedata[1].split('.')
    const isQuestion = !!boards.value.board.order_id
    let blank = '->';
    blank = blank.padStart(boards.value.board.depth * 3, " ")
    const to_detail = () => {
      // api.addCounting(data)
      api.fatchBoard(board_id.value)
      router.push({ name: 'BoardDetailView',params: {board_id: board_id.value} });
    }
    return {
      boards,
      api,
      day,
      time,
      isQuestion,
      blank,
      to_detail
    }
  }
}
</script>

<style scoped>
.td {
  text-align: center;
}
pre {
  margin: 0;
  cursor: pointer;
}
</style>
