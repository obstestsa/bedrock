import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Servers from '../views/Servers.vue';
import Environments from '../views/Environments.vue';
import Clusters from '../views/Clusters.vue';
import Products from '../views/Products.vue';
import OperatingSystems from '../views/OperatingSystems.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {
      plainLayout: true,
    },
  },
  {
    path: '/sor/server',
    name: 'server',
    component: Servers,
  },
  {
    path: '/sor/environment',
    name: 'environment',
    component: Environments,
  },
  {
    path: '/sor/cluster',
    name: 'cluster',
    component: Clusters,
  },
  {
    path: '/sor/product',
    name: 'product',
    component: Products,
  },
  {
    path: '/sor/os',
    name: 'operating-system',
    component: OperatingSystems,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
