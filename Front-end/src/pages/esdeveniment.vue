<template>
  <f7-page name="esdeveniment">
    <f7-navbar :title="esdeveniment.titol" back-link="Enrere"></f7-navbar>
    <f7-block-title>{{esdeveniment.titol}} - {{ esdeveniment.dataFi }} - {{ esdeveniment.hora }}</f7-block-title>
    <f7-block strong>
      {{esdeveniment.descripcio}}
    </f7-block>
    <f7-block>
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2986.4674564038014!2d2.439283715811632!3d41.537474879250595!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12a4b52028da6941%3A0x15c86152355e6371!2sPla%C3%A7a+de+Cuba%2C+08302+Matar%C3%B3%2C+Barcelona!5e0!3m2!1ses!2ses!4v1549728050487" width="100%" height="250" frameborder="0" style="border:0" allowfullscreen></iframe>
    </f7-block>
    <f7-block>
        <f7-list>
            <f7-list-item><b>Temàtica:</b> {{ esdeveniment.tematica }}</f7-list-item>
        </f7-list>
        <f7-list>
            <f7-list-button class="participar-button" color="white"><f7-icon material="person_pin"></f7-icon>&nbsp; Assistiré</f7-list-button>
        </f7-list>
    </f7-block>
    <f7-button class="chat-button" icon-material="chat" icon-size="35" large raised @click="$f7.panel.open('right', true)" disabled></f7-button>
  </f7-page>
</template>

<script>
  export default {
    data: function () {
      return {
        esdeveniment: {
            titol: 'Mercat de dissabte',
            dataFi: '11/02/2019',
            descripcio: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus rutrum commodo turpis ut pellentesque. Nunc fermentum cursus purus at maximus. Donec eget felis et augue mattis tempus. Vestibulum eleifend varius lacinia.',
            hora: '8:00',
            ubicacio: 'Pla d\'en Boet',
            tematica: 'Roba i complements'
        }
      };
    },

    created() {
        fetch('http://157.230.45.171:5000/api/esdeveniment/5', {
            method: 'GET'
        })
        .then(response => {
            return response.json();
        })
        .then(data => {
            this.esdeveniment = data;
        })
    }
  };
</script>
