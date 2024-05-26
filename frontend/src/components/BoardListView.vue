<template>
	<tr>
		<td class='td' v-if="!isQuestion" >Q</td>
    <td class='td' v-if="isQuestion" >A</td>
		<td>
		<c:choose>
		<c:otherwise>
			<router-link :to="{ name: 'BoardDetailView',params: {board_id: boards.board.id} }">{{boards.board.title}}</router-link>
		</c:otherwise>
		</c:choose>					
		</td>
		<td class='td'>{{boards.board.user_id.name}}</td>
		<td class='td'>{{day}} {{time[0]}}</td>
		<td class='td'>0</td>
	</tr>
</template>

<script>
import { ref } from 'vue';
import { useStore } from '@/stores/dev_test';
export default {
  props: ['board'],
  setup(props) {
    const test = useStore()
    const boards = ref(props)
    const timedata = (boards.value.board.created_at).split('T')
    const day = timedata[0]
    const time = timedata[1].split('.')
    const isQuestion = !!boards.value.board.order_id

    return {
      boards,
      test,
      day,
      time,
      isQuestion
    }
  }
}
</script>

<style scoped>
.td {
  text-align: center;
}
</style>
