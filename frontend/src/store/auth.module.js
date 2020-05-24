import ApiService from '../services/api.service';
import JwtService from '../services/jwt.service';
import mutation from './mutations.type';
import action from './actions.type';

const state = {
  user: {},
  isAuthenticated: !!JwtService.getToken(),
  error: null,
};

const getters = {
  getUser(state) {
    return state.user;
  },
  isAuthenticated(state) {
    return state.isAuthenticated;
  },
};

const mutations = {
  [mutation.SET_ERROR](state, error) {
    state.error = error;
  },
  [mutation.SET_AUTH](state, user) {
    state.isAuthenticated = true;
    state.user = { ...state.user, username: user.username, email: user.email };
    state.error = {};
    JwtService.setToken({
      access: user.access,
      refresh: user.refresh,
    });
  },
  [mutation.PURGE_AUTH](state) {
    state.isAuthenticated = false;
    state.user = {};
    state.error = {};
    JwtService.removeToken();
  },
};

const actions = {
  [action.LOGIN]({ commit }, { username, password }) {
    return new Promise(resolve => {
      ApiService.post('auth/token/', {
        username: username,
        password: password,
      })
        .then(({ data }) => {
          commit(mutation.SET_AUTH, data.user);
          resolve(data);
        })
        .catch(({ response, error }) => {
          if (response && response.data.message !== undefined) {
            commit(mutation.SET_ERROR, response);
            commit(mutation.SET_SNACKBAR, {
              message: response.data.message,
              color: 'error',
            });
          } else if (error) {
            commit(mutation.SET_ERROR, error.message);
            commit(mutation.SET_SNACKBAR, {
              message: error.message,
              color: 'error',
            });
          }
        });
    });
  },
  [action.LOGOUT]({ commit }) {
    commit(mutation.PURGE_AUTH);
    commit(mutation.SET_SNACKBAR, {
      message: 'Successfully Logged Out!',
      color: 'success',
    });
  },
  [action.CHECK_AUTH]({ commit, dispatch }) {
    if (JwtService.getToken()) {
      ApiService.setHeader();
      dispatch(action.REFRESH_AUTH);
    } else {
      commit(mutation.PURGE_AUTH);
    }
  },
  [action.REFRESH_AUTH]({ commit }) {
    return ApiService.post('auth/token/refresh/', {
      refresh: JwtService.getToken(JwtService.ID_REFRESH_TOKEN),
    })
      .then(({ data }) => {
        JwtService.setToken({ access: data.acess });
      })
      .catch(error => {
        commit(mutation.PURGE_AUTH);
        commit(mutation.SET_SNACKBAR, {
          message: 'Token Refresh Failed, Logged Out!',
          color: 'amber',
        });
      });
  },
};

export default {
  state,
  getters,
  mutations,
  actions,
};
