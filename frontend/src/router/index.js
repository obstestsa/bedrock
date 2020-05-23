import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Server from '../views/Server.vue';
import Environment from '../views/Environment.vue';
import ClusterList from '../views/ClusterList.vue';
import ApplicationList from '../views/ApplicationList.vue';
import OperatingSystemList from '../views/OperatingSystemList.vue';

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
    component: Server,
  },
  {
    path: '/sor/environment',
    name: 'environment',
    component: Environment,
  },
  {
    path: '/sor/cluster',
    name: 'cluster',
    component: ClusterList,
  },
  {
    path: '/sor/application',
    name: 'application',
    component: ApplicationList,
  },
  {
    path: '/sor/os',
    name: 'operating-system',
    component: OperatingSystemList,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
