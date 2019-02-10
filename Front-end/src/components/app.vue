<template>
<f7-app :params="f7params">
  <!-- Status bar overlay for fullscreen mode-->
  <f7-statusbar></f7-statusbar>

  <!-- Left panel with cover effect-->
  <f7-panel left cover class="theme-matconn">
    <f7-view>
      <f7-page>
        <img src="/static/img/logo.jpeg" alt="MATCONN">
        <f7-list>
          <f7-list-item title="Ajuntament" link="/ajuntament/" view="#view-home" @click="$f7.panel.close('left', true)"></f7-list-item>
          <f7-list-item title="Esports" link="/esports/" view="#view-home" @click="$f7.panel.close('left', true)"></f7-list-item>
          <f7-list-item title="Clubs" link="/clubs/" view="#view-home" @click="$f7.panel.close('left', true)"></f7-list-item>
          <f7-list-item title="Esdeveniments" link="/esdeveniments/" view="#view-home" @click="$f7.panel.close('left', true)"></f7-list-item>
        </f7-list>
      </f7-page>
    </f7-view>
  </f7-panel>


  <!-- Right panel with reveal effect-->
  <f7-panel right reveal>
    <f7-view>
      <f7-page>
        <f7-navbar title="Xat"></f7-navbar>
          <f7-messagebar ref="messagebar">
            <f7-link
              icon-ios="f7:arrow_up_fill"
              icon-md="material:send"
              slot="inner-end"
              placeholder="Missatge"></f7-link>
          </f7-messagebar>

          <f7-messages ref="messages">
            <f7-messages-title><b>9 de febrer</b> 12:58</f7-messages-title>
            <f7-message
              name="Xavi"
              :first="true"
              :tail="false"
            >
              <span slot="text" v-html="'Hola'"></span>
            </f7-message>
            <f7-message
              name="Xavi"
              :first="false"
              :tail="true"
            >
              <span slot="text" v-html="'Com funciona això?'"></span>
            </f7-message>
          </f7-messages>
      </f7-page>
    </f7-view>
  </f7-panel>


  <!-- Views/Tabs container -->
  <f7-views tabs class="safe-areas">
    <!-- Tabbar for switching views-tabs -->
    <f7-toolbar tabbar labels bottom>
      <f7-link tab-link="#view-home" tab-link-active icon-ios="f7:home_fil" icon-md="material:home" text="Home"></f7-link>
      <f7-link tab-link="#view-per-tu" icon-ios="f7:persons_round_fill" icon-md="material:record_voice_over" text="Per tu"></f7-link>
      <f7-link tab-link="#view-settings" icon-ios="f7:settings_fill" icon-md="material:settings" text="Configuració"></f7-link>
    </f7-toolbar>

    <!-- Your main view/tab, should have "view-main" class. It also has "tab-active" class -->
    <f7-view id="view-home" main tab tab-active url="/"></f7-view>

    <!-- Catalog View -->
    <f7-view id="view-per-tu" name="per-tu" tab url="/per-tu/"></f7-view>

    <!-- Settings View -->
    <f7-view id="view-settings" name="settings" tab url="/settings/"></f7-view>

  </f7-views>


  <!-- Popup -->
  <f7-popup id="my-popup">
    <f7-view>
      <f7-page>
        <f7-navbar title="Popup">
          <f7-nav-right>
            <f7-link popup-close>Close</f7-link>
          </f7-nav-right>
        </f7-navbar>
        <f7-block>
          <p>Popup content goes here.</p>
        </f7-block>
      </f7-page>
    </f7-view>
  </f7-popup>

  <f7-login-screen id="my-login-screen">
    <f7-view>
      <f7-page login-screen>
        <f7-login-screen-title>Login</f7-login-screen-title>
        <f7-list form>
          <f7-list-input
            type="text"
            name="username"
            placeholder="Your username"
            :value="username"
            @input="username = $event.target.value"
          ></f7-list-input>
          <f7-list-input
            type="password"
            name="password"
            placeholder="Your password"
            :value="password"
            @input="password = $event.target.value"
          ></f7-list-input>
        </f7-list>
        <f7-list>
          <f7-list-button title="Sign In" login-screen-close @click="alertLoginData"></f7-list-button>
          <f7-block-footer>
            Some text about login information.<br>Click "Sign In" to close Login Screen
          </f7-block-footer>
        </f7-list>
      </f7-page>
    </f7-view>
  </f7-login-screen>
</f7-app>
</template>
<script>

  import routes from '../js/routes.js';

  export default {
    data() {
      return {
        // Framework7 Parameters
        f7params: {
          name: 'MataroCity', // App name
          theme: 'auto', // Automatic theme detection
          // App root data
          data: function () {
            return {
              user: {
                firstName: 'John',
                lastName: 'Doe',
              },
              // Demo products for Catalog section
              products: [
                {
                  id: '1',
                  title: 'Apple iPhone 8',
                  description: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nisi tempora similique reiciendis, error nesciunt vero, blanditiis pariatur dolor, minima sed sapiente rerum, dolorem corrupti hic modi praesentium unde saepe perspiciatis.'
                },
                {
                  id: '2',
                  title: 'Apple iPhone 8 Plus',
                  description: 'Velit odit autem modi saepe ratione totam minus, aperiam, labore quia provident temporibus quasi est ut aliquid blanditiis beatae suscipit odio vel! Nostrum porro sunt sint eveniet maiores, dolorem itaque!'
                },
                {
                  id: '3',
                  title: 'Apple iPhone X',
                  description: 'Expedita sequi perferendis quod illum pariatur aliquam, alias laboriosam! Vero blanditiis placeat, mollitia necessitatibus reprehenderit. Labore dolores amet quos, accusamus earum asperiores officiis assumenda optio architecto quia neque, quae eum.'
                },
              ]
            };
          },

          // App routes
          routes: routes,

          // Register service worker
          serviceWorker: {
            path: '/service-worker.js',
          },
        },

        // Login screen data
        username: '',
        password: '',
      }
    },
    methods: {
      alertLoginData() {
        this.$f7.dialog.alert('Username: ' + this.username + '<br>Password: ' + this.password);
      },
    },
    mounted() {
      this.$f7ready((f7) => {

        // Call F7 APIs here
      });
    }
  }
</script>