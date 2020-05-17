import Vue from 'vue';
import Vuetify, { VTextField } from 'vuetify/lib';
import HeartIcon from '../components/HeartIcon.vue';

Vue.use(Vuetify, { components: { VTextField } });

export default new Vuetify({

  theme: {
    themes: {
      light: {
        primary: '#532594',
        secondary: '#5f5f5f',
        danger: '#e9444b',
      },
    },
  },
  icons: {
    values: {
      heart: {
        component: HeartIcon,
      },
    },
  },
});
