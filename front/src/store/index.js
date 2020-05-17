/* eslint-disable import/no-cycle */
import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';

import user from './modules/user.store';
import help from './modules/help.store';
import register from './modules/register.store';
import address from './modules/address.store';
import notification from './modules/notification.store';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    user,
    help,
    register,
    address,
    notification,
  },
  plugins: [
    createPersistedState({
      paths: ['register'],
    }),
  ],
});
