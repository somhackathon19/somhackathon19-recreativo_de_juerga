// Import Vue
import Vue from 'vue';

// Import Framework7
import Framework7 from 'framework7/framework7.esm.bundle.js';

// Import Framework7-Vue Plugin
import Framework7Vue from 'framework7-vue/framework7-vue.esm.bundle.js';

// Import Framework7 Styles
import 'framework7/css/framework7.bundle.css';

// Import Icons and App Custom Styles
import '../css/icons.css';
import '../css/app.scss';

// Import App Component
import App from '../components/app.vue';

// Init Framework7-Vue Plugin
Framework7.use(Framework7Vue)

// Init App
new Vue({
  el: '#app',
  render: (h) => h(App),

  // Register App Component
  components: {
    app: App
  },

  data() {
    return {
      tags: [
        {}
      ]
    }
  },

  created() {
    fetch('http://157.230.45.171:5000/api/etiquetes', {
      method: 'GET' 
    })
    .then(response => {
      return response.json();
    })
    .then(data => {
      this.tags = data;
    })
  },

  methods: {
    fixDate(date) {
      if(date) {
        let arrDate = date.split('-');
        return `${arrDate[2]}/${arrDate[1]}/${arrDate[0]}`;
      } else {
        return '';
      }
    }
  }
});