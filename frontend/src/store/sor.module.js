import { SorApiService } from '../services/api.service';
import mutation from './mutations.type';
import action from './actions.type';

const state = {
  servers: [],
  environments: [],
  clusters: [],
  products: [],
  loading: true,
  error: null,
};

const getters = {
  isLoading(state) {
    return state.loading;
  },
  getResource: state => type => {
    return state[type];
  },
  getResourceByField: state => (type, field, value) => {
    return state[type].filter(resource => {
      if (Array.isArray(resource[field])) {
        return resource[field].includes(value);
      }
      return resource[field] === value;
    });
  },
};

const mutations = {
  [mutation.FETCH_PENDING](state, status) {
    state.loading = status;
  },
  [mutation.SET_RESOURCES](state, { type, resources }) {
    state[type] = resources;
  },
  [mutation.RESOURCE_ADD](state, { type, resource }) {
    state[type].push(resource);
  },
  [mutation.RESOURCE_EDIT](state, { type, updatedResource }) {
    const index = state[type].findIndex(
      resource => resource.id === updatedResource.id
    );
    Object.assign(state[type][index], updatedResource);
  },
  [mutation.RESOURCE_REMOVE](state, { type, id }) {
    const index = state[type].findIndex(resource => resource.id === id);
    state[type].splice(index, 1);
  },
};

const actions = {
  [action.FETCH_RESOURCES]({ commit }, type) {
    commit(mutation.FETCH_PENDING, true);
    return SorApiService.get(type)
      .then(response => {
        commit(mutation.SET_RESOURCES, {
          type: type,
          resources: response.data,
        });
      })
      .catch(error => {
        commit(mutation.SET_SNACKBAR, {
          message: error.message,
          color: 'error',
        });
      })
      .then(() => {
        commit(mutation.FETCH_PENDING, false);
      });
  },
  [action.RESOURCE_CREATE]({ commit }, { type, resource }) {
    commit(mutation.FETCH_PENDING, true);
    return SorApiService.post(type, resource)
      .then(response => {
        commit(mutation.RESOURCE_ADD, {
          type: type,
          resource: response.data,
        });
      })
      .catch(error => {
        commit(mutation.SET_SNACKBAR, {
          message: error.message,
          color: 'error',
        });
      })
      .then(() => {
        commit(mutation.FETCH_PENDING, false);
      });
  },
  [action.RESOURCE_UPDATE]({ commit }, { type, resource }) {
    commit(mutation.FETCH_PENDING, true);
    return SorApiService.update(type, resource.id, resource)
      .then(response => {
        commit(mutation.RESOURCE_EDIT, {
          type: type,
          updatedResource: response.data,
        });
      })
      .catch(error => {
        commit(mutation.SET_SNACKBAR, {
          message: error.message,
          color: 'error',
        });
      })
      .then(() => {
        commit(mutation.FETCH_PENDING, false);
      });
  },
  [action.RESOURCE_DELETE]({ commit }, { type, id }) {
    commit(mutation.FETCH_PENDING, true);
    return SorApiService.delete(`${type}/${id}`)
      .then(response => {
        commit(mutation.FETCH_PENDING, false);
        commit(mutation.RESOURCE_REMOVE, { type: type, id: id });
      })
      .catch(error => {
        commit(mutation.SET_SNACKBAR, {
          message: error.message,
          color: 'error',
        });
      })
      .then(() => {
        commit(mutation.FETCH_PENDING, false);
      });
  },
};

export default {
  state,
  getters,
  mutations,
  actions,
};
