import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import About from '../views/About.vue';
import CreateAccount from '../views/CreateAccount.vue';
import CreateHelp from '../views/CreateHelp.vue';

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
  
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
