import Vue from 'vue';
import VueRouter from 'vue-router';
// eslint-disable-next-line import/no-cycle
import store from '../store/index';

Vue.use(VueRouter);

const guard = (to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('userInfo');
  if (isAuthenticated) {
    if (!store.getters['user/getUser']) {
      store.dispatch('user/getCurrentUser').then(() => next());
    } else {
      next();
    }
  } else next('/login');
};
const notGuard = (to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('userInfo');
  if (!isAuthenticated) next();
  else next('/');
};

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue'),
    beforeEnter: notGuard,
  },
  {
    path: '/create-account',
    name: 'CreateAccount',
    component: () => import('../views/CreateAccount.vue'),
    beforeEnter: notGuard,
  },
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue'),
    beforeEnter: guard,
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue'),
    beforeEnter: guard,
  },
  {
    path: '/create-help',
    name: 'CreateHelp',
    component: () => import('../views/CreateHelp.vue'),
    beforeEnter: guard,
  },
  {
    path: '/how-to',
    name: 'HowTo',
    component: () => import('../views/HowTo.vue'),
    beforeEnter: guard,
  },
  {
    path: '/help-details',
    name: 'HelpDetails',
    component: () => import('../views/HelpDetails.vue'),
    beforeEnter: guard,
  },
  {
    path: '/help-on-going',
    name: 'HelpOnGoing',
    component: () => import('../views/HelpOnGoing.vue'),
    beforeEnter: guard,
  },
  {
    path: '/volunteer-details',
    name: 'VolunteerDetails',
    component: () => import('../views/VolunteerDetails.vue'),
    beforeEnter: guard,
  },
  {
    path: '/user-details',
    name: 'UserDetails',
    component: () => import('../views/UserDetails.vue'),
    beforeEnter: guard,
  },
  {
    path: '/list-helpextended',
    name: 'ListHelpExtended',
    component: () => import('../views/ListHelpExtended.vue'),
    beforeEnter: guard,
  },
  {
    path: '/requested-helps',
    name: 'RequestedHelps',
    component: () => import('../views/RequestedHelps.vue'),
    beforeEnter: guard,
  },
  {
    path: '/requested-helps-user',
    name: 'RequestedHelpsUser',
    component: () => import('../views/RequestedHelpsUser.vue'),
    beforeEnter: guard,
  },
  {
    path: '/forgot-user-pass',
    name: 'ForgotUserPass',
    component: () => import('../views/ForgotUserPass.vue'),
    beforeEnter: notGuard,
  },
  {
    path: '/regenerate-user-pass',
    name: 'RegenerateUserPass',
    component: () => import('../views/RegenerateUserPass.vue'),
    beforeEnter: notGuard,
  },
  {
    path: '*',
    redirect: '/login',
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
