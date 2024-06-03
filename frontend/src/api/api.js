const HOST = process.env.VUE_APP_API_URL

const ACCOUNTS = 'accounts/'
const BOARDS = 'boards/'
// const COMMENTS = 'comment/'


export default {
  accounts: {
    signup: () => HOST + ACCOUNTS + 'user/signup/', 
    login: () => HOST + ACCOUNTS + 'user/login/', 
    logout: () => HOST + ACCOUNTS + 'user/logout/',
    reissue: () => HOST + ACCOUNTS + 'user/reissue/',
  },
  boards: {
    boards_detail_update_delete: board_id => HOST + BOARDS + `${board_id}/`, 
    boards_list: () => HOST + BOARDS + 'list/',
    boards_create: () => HOST + BOARDS + 'create/',
    boards_counting: board_id => HOST + BOARDS + 'counting/' + `${board_id}/`,
  }
}
