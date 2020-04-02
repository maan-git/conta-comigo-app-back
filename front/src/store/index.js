import Vue from 'vue';
import Vuex from 'vuex';

import user from './modules/user.store';
import help from './modules/help.store';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    user,
    help,
  },
});
