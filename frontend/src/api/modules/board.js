import { BASE_URL } from '@/api/base'

export function getItem(params) {
  return BASE_URL.get('path', {
    params,
    headers: {},
  })
    .then((result) => {
      return result.data
    })
}

export function addItem(params) {
  return BASE_URL.post('path',
    params,
    {
      headers: {}
    }).then((result) => {
      return result.data
    })
}

export function updateItem(params) {
  return BASE_URL.put('path',
    params,
    {
      headers: {}
    }).then((result) => {
      return result.data
    })
}

export function removeItem(params) {
  return BASE_URL.delete('path', {
    headers: {},
    data: params,
  }).then((result) => {
    return result.data
  })
}