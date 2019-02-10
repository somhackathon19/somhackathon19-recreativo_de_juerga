// App pages
import HomePage from '../pages/home.vue';
import EsportsPage from '../pages/esports.vue';
import AjuntamentPage from '../pages/ajuntament.vue';
import ClubsPage from '../pages/clubs.vue';
import EsdevenimentsPage from '../pages/esdeveniments.vue';
import PerTuPage from '../pages/per-tu.vue';

// Event pages
import EsportPage from '../pages/esport.vue';
import ClubPage from '../pages/club.vue';
import EsdevenimentPage from '../pages/esdeveniment.vue';
import ContacteAjuntamentPage from '../pages/contacte-ajuntament.vue';
import AfegirEsportPage from '../pages/afegir-esport.vue';
import AfegirClubPage from '../pages/afegir-club.vue';
import AfegirEsdevenimentPage from '../pages/afegir-esdeveniment.vue';

// Ajuntament pages
import AgendaCulturalPage from '../pages/agenda-cultural.vue';
import AgendaCulturalArticlePage from '../pages/agenda-cultural-article.vue';
import AvisosPage from '../pages/avisos.vue';

// Boilerplate
import AboutPage from '../pages/about.vue';
import FormPage from '../pages/form.vue';
import CatalogPage from '../pages/catalog.vue';
import SettingsPage from '../pages/settings.vue';

import DynamicRoutePage from '../pages/dynamic-route.vue';
import RequestAndLoad from '../pages/request-and-load.vue';
import NotFoundPage from '../pages/404.vue';

var routes = [
  {
    path: '/',
    component: HomePage,
  },
  {
    path: '/about/',
    component: AboutPage,
  },
  {
    path: '/form/',
    component: FormPage,
  },
  {
    path: '/per-tu/',
    component: PerTuPage,
  },
  {
    path: '/ajuntament/',
    component: AjuntamentPage,
  },
  {
    path: '/agenda-cultural/',
    component: AgendaCulturalPage,
  },
  {
    path: '/agenda-cultural/:id',
    component: AgendaCulturalArticlePage,
  },
  {
    path: '/esports/',
    component: EsportsPage,
  },
  {
    path: '/clubs/',
    component: ClubsPage,
  },
  {
    path: '/esdeveniments/',
    component: EsdevenimentsPage,
  },
  {
    path: '/esport/:id/',
    component: EsportPage,
  },
  {
    path: '/club/:id/',
    component: ClubPage,
  },
  {
    path: '/esdeveniment/:id/',
    component: EsdevenimentPage,
  },
  {
    path: '/avisos/',
    component: AvisosPage,
  },
  {
    path: '/contacte-ajuntament/',
    component: ContacteAjuntamentPage,
  },
  {
    path: '/settings/',
    component: SettingsPage,
  },
  {
    path: '/afegir-esport/',
    component: AfegirEsportPage,
  },
  {
    path: '/afegir-club/',
    component: AfegirClubPage,
  },
  {
    path: '/afegir-esdeveniment/',
    component: AfegirEsdevenimentPage,
  },
  {
    path: '/dynamic-route/blog/:blogId/post/:postId/',
    component: DynamicRoutePage,
  },
  {
    path: '/request-and-load/user/:userId/',
    async: function (routeTo, routeFrom, resolve, reject) {
      // Router instance
      var router = this;

      // App instance
      var app = router.app;

      // Show Preloader
      app.preloader.show();

      // User ID from request
      var userId = routeTo.params.userId;

      // Simulate Ajax Request
      setTimeout(function () {
        // We got user data from request
        var user = {
          firstName: 'Vladimir',
          lastName: 'Kharlampidi',
          about: 'Hello, i am creator of Framework7! Hope you like it!',
          links: [
            {
              title: 'Framework7 Website',
              url: 'http://framework7.io',
            },
            {
              title: 'Framework7 Forum',
              url: 'http://forum.framework7.io',
            },
          ]
        };
        // Hide Preloader
        app.preloader.hide();

        // Resolve route to load page
        resolve(
          {
            component: RequestAndLoad,
          },
          {
            context: {
              user: user,
            }
          }
        );
      }, 1000);
    },
  },
  {
    path: '(.*)',
    component: NotFoundPage,
  },
];

export default routes;
