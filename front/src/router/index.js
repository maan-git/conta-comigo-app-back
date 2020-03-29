import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import About from '../views/About.vue';
import CreateAccount from '../views/CreateAccount.vue';
import CreateHelp from '../views/CreateHelp.vue';
import ListHelp from '../views/ListHelp.vue';
import HowTo from '../views/HowTo.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/about',
    name: 'About',
    component: About,
  },
  {
    path: '/create-account',
    name: 'CreateAccount',
    component: CreateAccount,
  },
  {
    path: '/create-help',
    name: 'CreateHelp',
    component: CreateHelp,
  },
  {
    path: '/list-help',
    name: 'ListHelp',
    component: ListHelp,
  },
  {
    path: '/how-to',
    name: 'HowTo',
    component: HowTo,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
