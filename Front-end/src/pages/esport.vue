<template>
  <f7-page name="esport">
    <f7-navbar :title="esport.titol" back-link="Enrere"></f7-navbar>
    <f7-block-title>{{esport.titol}} - {{ esport.dataFi }} - {{ esport.hora }}</f7-block-title>
    <f7-block strong>
      {{esport.descripcio}}
    </f7-block>
    <f7-block>
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d11947.003674407208!2d2.4237706436657445!3d41.5313357680182!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12a4b4e36fb894e1%3A0xa73eeabfe82632de!2sPlacita+d&#39;en+Boet%2C+08302+Matar%C3%B3%2C+Barcelona!5e0!3m2!1ses!2ses!4v1549715865247" width="100%" height="250" frameborder="0" style="border:0" allowfullscreen></iframe>
    </f7-block>
    <f7-block>
        <f7-list>
            <f7-list-item>Participants: {{ esport.rang }} | {{esport.participants}} confirmats</f7-list-item>
        </f7-list>
        <f7-list>
            <f7-list-button :id="`btn-join-esport-${1}`" class="participar-button" color="white" @click="join()"><f7-icon :material="joinButton.iconClass"></f7-icon>&nbsp; {{ joinButton.text }}</f7-list-button>
        </f7-list>
    </f7-block>
    <f7-button :id="`btn-chat-esport-${1}`" class="chat-button" icon-material="chat" icon-size="35" large raised @click="$f7.panel.open('right', true)" disabled></f7-button>
  </f7-page>
</template>

<script>
  export default {
    data: function () {
      return {
        esport: {
            titol: 'Torneig de bàsquet 3x3',
            dataFi: '11/02/2019',
            descripcio: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus rutrum commodo turpis ut pellentesque. Nunc fermentum cursus purus at maximus. Donec eget felis et augue mattis tempus. Vestibulum eleifend varius lacinia.',
            hora: '17:00',
            ubicacio: 'Pla d\'en Boet',
            rang: '10 - 30',
            participants: '15'
        },
        joinButton: {
          iconClass: 'person_pin',
          text: 'Participar'
        }
      };
    },

    methods: {
      join() {
        document.getElementById(`btn-chat-esport-${1}`).classList.remove('disabled');
        document.getElementById(`btn-join-esport-${1}`).classList.add('joined');
        document.querySelector(`#btn-join-esport-${1} > a`).classList.add('disabled');
        this.joinButton.iconClass = 'done';
        this.joinButton.text = 'Participant';
      }
    },

    created() {
        fetch('http://157.230.45.171:5000/api/esdeveniment/esport/1', {
            method: 'GET'
        })
        .then(response => {
            return response.json();
        })
        .then(data => {
            this.esport = data;
        })
    }
  };
</script>
