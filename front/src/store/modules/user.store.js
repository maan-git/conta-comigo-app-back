/* eslint-disable no-shadow */
import api from '../api';

const SET_USER = 'SET_USER';
const SET_USER_LOADING = 'SET_USER_LOADING';
const SET_USER_ERROR = 'SET_USER_ERROR';
const SET_TOKEN = 'SET_TOKEN';
const SET_LOGIN_ERROR = 'SET_LOGIN_ERROR';
const SET_LOGIN_LOADING = 'SET_LOGIN_LOADING';
const SET_USERS = 'SET_USERS';
const SET_USERS_ERROR = 'SET_USERS_ERROR';
const SET_USERS_LOGIN_LOADING = 'SET_USERS_LOGIN_LOADING';
const SET_VOLUNTEER_DETAILS = 'SET_VOLUNTEER_DETAILS';
const SET_VOLUNTEER_DETAILS_ERROR = 'SET_VOLUNTEER_DETAILS_ERROR';
const SET_VOLUNTEER_DETAILS_LOADING = 'SET_VOLUNTEER_DETAILS_LOADING';
const SET_USER_ADDRESS = 'SET_USER_ADDRESS';
const SET_USER_ADDRESS_ERROR = 'SET_USER_ADDRESS_ERROR';
const SET_USER_ADDRESS_LOADING = 'SET_USER_ADDRESS_LOADING';
const SET_FORGOT_USER_PASS_SUCCESS = 'SET_FORGOT_USER_PASS_SUCCESS';

const state = {
  user: null,
  userLoading: false,
  userError: null,
  token: '',
  loginError: null,
  loginLoading: false,
  users: null,
  usersError: null,
  usersLoginLoading: false,

  volunteerDetails: null,
  volunteerDetailsError: null,
  volunteerDetailsLoading: false,

  userAddress: null,
  userAddressError: null,
  userAddressLoading: false,

  forgotUserPassLoading: false,
  forgotUserPassError: null,
  forgotUserPassSuccess: false,
};

const getters = {
  getUser(state) { return state.user; },
  getToken(state) { return state.token; },
  getLoginError(state) { return state.loginError; },
  getLoginLoading(state) { return state.loginLoading; },
  getUsers(state) { return state.users; },
  getUsersError(state) { return state.usersError; },
  getUsersLoginLoading(state) { return state.usersLoginLoading; },
  getVolunteerDetailsError(state) { return state.volunteerDetailsError; },
  getVolunteerDetailsLoading(state) { return state.volunteerDetailsLoading; },
  getUsersAddressError(state) { return state.userAddressError; },
  getUsersAddressLoading(state) { return state.userAddressLoading; },
};

const actions = {
  setUserInfo({ commit }, data) {
    const expDate = Date.now();
    // xpd stands for expiration Date
    Object.assign(data, { xpd: expDate });
    localStorage.setItem('userInfo', JSON.stringify(data));
    commit(SET_USER, data);
  },
  login({ commit, dispatch }, data) {
    commit(SET_LOGIN_LOADING, true);
    return api().post('app/login/', data).then((success) => {
      // dispatch('setUserInfo', success.data);
      commit(SET_TOKEN, success);
      commit(SET_LOGIN_ERROR, null);
      commit(SET_LOGIN_LOADING, false);
      return dispatch('getCurrentUser');
    }).catch((error) => {
      if (error.response.data.detail) commit(SET_LOGIN_ERROR, error.response.data.detail);
      else commit(SET_LOGIN_ERROR, error.response.statusText);
      commit(SET_LOGIN_LOADING, false);
    });
  },

  logout({ commit }) {
    return api().post('app/logout/').then(() => {
      commit(SET_USER, null);
      commit(SET_TOKEN, null);
      localStorage.removeItem('userInfo');
    });
  },

  register({ commit }) {
    commit(SET_LOGIN_LOADING, true);
  },
  regeneratePass({ commit }) {
    commit(SET_FORGOT_USER_PASS_SUCCESS, true);
  },
  getCurrentUser({ commit, dispatch }) {
    commit(SET_LOGIN_LOADING, false);
    return api().get('app/user/current/').then((success) => {
      dispatch('setUserInfo', success.data);
    }).catch((error) => {
      localStorage.removeItem('userInfo');
      commit(SET_LOGIN_ERROR, error.response.data.error);
    });
  },

  getUsers({ commit }, queryparams) {
    commit(SET_USERS_LOGIN_LOADING, true);
    let url = 'app/user/';
    if (queryparams) { url += `?${queryparams}`; }
    return api().get(url).then((success) => {
      commit(SET_USERS_ERROR, null);
      commit(SET_USERS_LOGIN_LOADING, false);
      commit(SET_USERS, success.data.results);
    }).catch((error) => {
      if (error.response.data.detail) commit(SET_USERS_ERROR, error.response.data.detail);
      else commit(SET_USERS_ERROR, error.response.statusText);
      commit(SET_USERS_LOGIN_LOADING, false);
    });
  },
  getVolunteerDetails({ commit }, id) {
    commit(SET_VOLUNTEER_DETAILS_LOADING, true);
    return api().get(`/app/user/${id}/`).then((success) => {
      commit(SET_VOLUNTEER_DETAILS_ERROR, null);
      commit(SET_VOLUNTEER_DETAILS_LOADING, false);
      commit(SET_VOLUNTEER_DETAILS, success.data);
    }).catch((error) => {
      if (error.response.data) commit(SET_VOLUNTEER_DETAILS_ERROR, error.response.data);
      else commit(SET_VOLUNTEER_DETAILS_ERROR, error.response.statusText);
      commit(SET_VOLUNTEER_DETAILS_LOADING, false);
    });
  },
  getUserAddress({ commit }, id) {
    commit(SET_USER_ADDRESS_LOADING, true);
    return api().get(`app/user/${id}/getaddresses/`).then((success) => {
      commit(SET_USER_ADDRESS_ERROR, null);
      commit(SET_USER_ADDRESS_LOADING, false);
      commit(SET_USER_ADDRESS, success.data[0]);
    }).catch((error) => {
      if (error.response.data) commit(SET_USER_ADDRESS_ERROR, error.response.data);
      else commit(SET_USER_ADDRESS_ERROR, error.response.statusText);
      commit(SET_USER_ADDRESS_LOADING, false);
    });
  },
  /** Edit User Methods */
  updatePersonalData({ commit, state, dispatch }, data) {
    commit(SET_USER_LOADING, true);
    return api().patch(`app/user/${state.user.id}/`, data).then((success) => {
      commit(SET_USER_ERROR, null);
      commit(SET_USER_LOADING, false);
      commit(SET_USER, success.data);
      dispatch('getCurrentUser');
    }).catch((error) => {
      if (error.response.data.detail) commit(SET_USER_ERROR, error.response.data.detail);
      else commit(SET_USER_ERROR, error.response.statusText);
      commit(SET_USER_LOADING, false);
    });
  },
  updateAddress({ commit, state, dispatch }, data) {
    return api().patch(`app/user/${state.user.id}/updateaddress/`, data).then(() => {
      commit(SET_USER_ERROR, null);
      commit(SET_USER_LOADING, false);
      dispatch('getCurrentUser');
    }).catch((error) => {
      if (error.response.data.detail) commit(SET_USER_ERROR, error.response.data.detail);
      else commit(SET_USER_ERROR, error.response.statusText);
      commit(SET_USER_LOADING, false);
    });
  },
  clearUserUtils({ commit }) {
    commit(SET_USER_LOADING, false);
    commit(SET_USER_ERROR, null);
  },
};

const mutations = {
  [SET_USER](state, value) {
    state.user = value;
  },
  [SET_USER_LOADING](state, value) {
    state.userLoading = value;
  },
  [SET_USER_ERROR](state, value) {
    state.userError = value;
  },
  [SET_TOKEN](state, value) {
    state.token = value;
  },
  [SET_LOGIN_ERROR](state, value) {
    state.loginError = value;
  },
  [SET_LOGIN_LOADING](state, value) {
    state.loginLoading = value;
  },
  [SET_USERS](state, value) {
    state.users = value;
  },
  [SET_USERS_ERROR](state, value) {
    state.usersError = value;
  },
  [SET_USERS_LOGIN_LOADING](state, value) {
    state.usersLoginLoading = value;
  },
  [SET_VOLUNTEER_DETAILS](state, value) {
    state.volunteerDetails = value;
  },
  [SET_VOLUNTEER_DETAILS_ERROR](state, value) {
    state.volunteerDetailsError = value;
  },
  [SET_VOLUNTEER_DETAILS_LOADING](state, value) {
    state.volunteerDetailsLoading = value;
  },
  [SET_USER_ADDRESS](state, value) {
    state.userAddress = value;
  },
  [SET_USER_ADDRESS_ERROR](state, value) {
    state.userAddressError = value;
  },
  [SET_USER_ADDRESS_LOADING](state, value) {
    state.userAddressLoading = value;
  },
  [SET_FORGOT_USER_PASS_SUCCESS](state, value) {
    state.forgotUserPassSuccess = value;
  },
};


export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
