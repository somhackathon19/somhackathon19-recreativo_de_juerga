<style >
  img {
    max-width: 100%;
    text-align: center;
  }
</style>

<template>
  <f7-page name="club">
    <f7-navbar :title="club.titol" back-link="Enrere"></f7-navbar>
    <f7-block-title>{{club.titol}}</f7-block-title>
    <f7-block strong>
      {{club.descripcio}}
    </f7-block>
    <f7-block>
      <img src="/static/img/ajedrez.jpg" :alt="club.titol">
    </f7-block>
    <f7-block>
        <f7-list>
            <f7-list-item>{{club.membres}} membres</f7-list-item>
        </f7-list>
        <f7-list>
            <f7-list-button class="participar-button" color="white"><f7-icon material="person_pin"></f7-icon>&nbsp; Subscripció</f7-list-button>
        </f7-list>
    </f7-block>
    <f7-button class="chat-button" icon-material="chat" icon-size="35" large raised @click="$f7.panel.open('right', true)" disabled></f7-button>
  </f7-page>
</template>

<script>
  export default {
    data: function () {
      return {
        club: {
            titol: 'Club d\'Escacs (amateur)',
            descripcio: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus rutrum commodo turpis ut pellentesque. Nunc fermentum cursus purus at maximus. Donec eget felis et augue mattis tempus. Vestibulum eleifend varius lacinia.',
            membres: '65',
            img: 'link/to/img'
        },
      };
    },

    created() {
        fetch('http://157.230.45.171:5000/api/esdeveniment/club/4', {
            method: 'GET'
        })
        .then(response => {
            return response.json();
        })
        .then(data => {
            this.club = data;
        })
    }
  };
</script>
