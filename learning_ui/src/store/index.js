import Vue from 'vue'
import Vuex from 'vuex'

import exam from './modules/exam'

import VuexPersistence from 'vuex-persist'
Vue.use(Vuex)

const vuexLocal = new VuexPersistence({
  storage: window.localStorage
})

const store = new Vuex.Store({
  modules: {
    exam,
  },
  plugins: [vuexLocal.plugin]
})

export default store;