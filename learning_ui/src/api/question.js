import api from './base'

const create = (data) => api.baseApi({
  method: 'POST',
  url: `exam/question/`,
  data: data
})
const list = (data = null) => api.baseApi({
  method: 'GET',
  url: `exam/question/`,
  data: data
})

export default {
  create,
  list
}