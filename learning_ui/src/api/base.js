import Vue from 'vue'
// import handleErrors from '../utils/handleErrors'
// import store from '../store/index'
// import constance from '../constance/const'
// const URL = constance.URL

const baseApi = async (data) => {
  const options = {
    method: data.method,
    url: "http://127.0.0.1:8000/" + data.url,
    data: data.data,
    // headers: {
    //   Authorization: 'Bearer ' + store.getters.token
    // },
    "Content-Type": data.contentType ? data.contentType : "application/json"
  };

  return Vue.axios(options)
    .then((response) => {
      // handleErrors.showError(response.data, true)
      window.scrollTo(0, 0);
      return response.data
    }).catch((error) => {
      console.log(error)
      // handleErrors.showError(error.response.data, false)
    })
}

export default {
  baseApi
}