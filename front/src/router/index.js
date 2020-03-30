import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue'),
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue'),
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue'),
  },
  {
    path: '/create-account',
    name: 'CreateAccount',
    component: () => import('../views/CreateAccount.vue'),
  },
  {
    path: '/create-help',
    name: 'CreateHelp',
    component: () => import('../views/CreateHelp.vue'),
  },
  {
    path: '/list-help',
    name: 'ListHelp',
    component: () => import('../views/ListHelp.vue'),
  },
  {
    path: '/how-to',
    name: 'HowTo',
    component: () => import('../views/HowTo.vue'),
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
