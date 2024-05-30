const HOST = process.env.VUE_APP_API_URL

const ACCOUNTS = 'accounts/'
const BOARDS = 'boards/'
// const COMMENTS = 'comment/'


export default {
  accounts: {
    signup_signout: () => HOST + ACCOUNTS + 'user/signup/', //get, post, delete
    login: () => HOST + ACCOUNTS + 'user/login/', //post
    logout: () => HOST + ACCOUNTS + 'user/logout/',
    reissue: () => HOST + ACCOUNTS + 'user/reissue/',
  },
  boards: {
    boards_detail_update_delete: board_id => HOST + BOARDS + `${board_id}/`, //get, patch
    boards_list: () => HOST + BOARDS + 'list/',
    boards_create: () => HOST + BOARDS + 'create/',
    boards_counting: board_id => HOST + BOARDS + 'counting/' + `${board_id}/`,
    // comments_list: board_id => HOST + BOARDS + COMMENTS + `${board_id}/`, // get
    // comment_delete: (board_id, comment_id) => HOST + BOARDS + `${board_id}/` + COMMENTS + `${comment_id}/`, //delete
  }
}
