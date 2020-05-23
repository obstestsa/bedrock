import Vue from 'vue';
import Vuex from 'vuex';
import sor from './sor.module';
import auth from './auth.module';
import snackBar from './snackbar.module';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    sor,
    auth,
    snackBar,
  },
});
