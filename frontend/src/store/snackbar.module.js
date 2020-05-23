import { SET_SNACKBAR } from './mutations.type';

const state = {
  message: '',
  color: '',
};

const mutations = {
  [SET_SNACKBAR](state, { message, color }) {
    state.message = message;
    state.color = color;
  },
};

export default {
  state,
  mutations,
};
