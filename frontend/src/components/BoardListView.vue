<template>
	<tr>
		<td>{{boards.board.id}}</td>
		<td>
		<c:choose>
		<c:otherwise>
			<router-link :to="{ name: 'BoardDetailView',params: {board_id: boards.board.id} }">{{boards.board.title}}</router-link>
		</c:otherwise>
		</c:choose>					
		</td>
		<td>{{boards.board.user_id.name}}</td>
		<td>{{boards.board.created_at}}</td>
		<td>0</td>
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
    return {
      boards,
      test
    }
  }
}
</script>