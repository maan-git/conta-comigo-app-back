/* eslint-disable no-shadow */
import api from '../api';

const SET_ADDRESS_LOADING = 'SET_ADDRESS_LOADING';
const SET_ADDRESS_ERROR = 'SET_ADDRESS_ERROR';
const SET_CEP = 'SET_CEP';
const SET_ENDERECO = 'SET_ENDERECO';
const SET_BAIRRO = 'SET_BAIRRO';
const SET_BAIRROS = 'SET_BAIRROS';
const SET_CIDADE = 'SET_CIDADE';
const SET_ESTADO = 'SET_ESTADO';


const state = {
  cep: '',
  endereco: '',
  bairro: '',
  bairros: [],
  cidade: '',
  estado: '',

  addressLoading: false,
  addressError: null,
};


const actions = {
  findByZip({ commit, dispatch }, cep) {
    const zip = cep.replace('-', '');
    commit(SET_ADDRESS_LOADING, true);
    return api().get(`/app/address/findbyzip/?zip=${zip}`).then((s) => {
      commit(SET_CEP, zip);
      commit(SET_ENDERECO, s.data.address);
      if (s.data.neighborhood.description && s.data.neighborhood.description.length > 0) {
        commit(SET_BAIRROS, [s.data.neighborhood]);
        commit(SET_BAIRRO, s.data.neighborhood.id);
      } else if (s.data.city.id) {
        dispatch('findNeighborhood', s.data.city.id);
      } else {
        commit(SET_BAIRROS, []);
        commit(SET_BAIRRO, '');
      }
      commit(SET_CIDADE, s.data.city.description);
      commit(SET_ESTADO, s.data.state.description);
      commit(SET_ADDRESS_LOADING, false);
    }).catch((error) => {
      commit(SET_ADDRESS_LOADING, false);
      if (error.response.data.detail) commit(SET_ADDRESS_ERROR, error.response.data.detail);
      else commit(SET_ADDRESS_ERROR, error.response.statusText);
    });
  },
  findNeighborhood({ commit }, cityid) {
    commit(SET_ADDRESS_LOADING, true);
    return api().get(`/app/neighborhood/?city_id=${cityid}`).then((s) => {
      commit(SET_BAIRROS, s.data.results);
      commit(SET_ADDRESS_LOADING, false);
    }).catch((error) => {
      commit(SET_ADDRESS_LOADING, false);
      if (error.response.data.detail) commit(SET_ADDRESS_ERROR, error.response.data.detail);
      else commit(SET_ADDRESS_ERROR, error.response.statusText);
    });
  },
};

const mutations = {
  [SET_ADDRESS_LOADING](state, value) {
    state.addressLoading = value;
  },
  [SET_ADDRESS_ERROR](state, value) {
    state.addressError = value;
  },
  [SET_CEP](state, value) {
    state.cep = value;
  },
  [SET_ENDERECO](state, value) {
    state.endereco = value;
  },
  [SET_BAIRRO](state, value) {
    state.bairro = value;
  },
  [SET_BAIRROS](state, value) {
    state.bairros = value;
  },
  [SET_CIDADE](state, value) {
    state.cidade = value;
  },
  [SET_ESTADO](state, value) {
    state.estado = value;
  },
};


export default {
  namespaced: true,
  state,
  actions,
  mutations,
};
