import { BASE_URL } from '@/api/base'
import { URLS } from '@/api/urls'

export async function getBoard(board_id) {
  params = {
    board_id: board_id
  }
  const result = await BASE_URL.get(URLS.board, {
    params,
    headers: {},
  })
  return result.data
}

"board_id, board_name, board_description, id_busstop_yandex, id_tramstop_yandex, zabbix_node_name, id_busstop_pikas, id_tramstop_pikas, boards_data, datatime_update_pikas"

export async function addBoard(board_data) {
  const result = await BASE_URL.post('path',
    board_data,
    {
      headers: {}
    })
  return result.data
}

export async function updateBoard(board_data) {
  const result = await BASE_URL.put('path',
    params,
    {
      headers: {}
    })
  return result.data
}

export async function removeBoard(board_id) {
  const result = await BASE_URL.delete('path', {
    headers: {},
    data: {board_id: board_id},
  })
  return result.data
}