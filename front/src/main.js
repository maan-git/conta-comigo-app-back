import VueMask from 'v-mask';

import Vue from 'vue';
import * as validation from './utils/validation';
import App from './App.vue';
import './registerServiceWorker';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';
import '@babel/polyfill';

Vue.config.productionTip = false;
Vue.use(VueMask);

Vue.prototype.$vln = validation;

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount('#app');
