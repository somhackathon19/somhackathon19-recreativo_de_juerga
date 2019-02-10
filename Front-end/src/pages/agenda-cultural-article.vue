<style >
  img {
    max-width: 100%;
    text-align: center;
  }
</style>

<template>
  <f7-page name="agenda-cultural-article">
    <f7-navbar :title="agenda.titol" back-link="Back"></f7-navbar>
    <f7-block-title>{{agenda.titol}}</f7-block-title>
        <f7-block>
      <img src="/static/img/cultural1.JPG" :alt="agenda.titol">
    </f7-block>
    <f7-block strong>
      {{agenda.descripcio}}
    </f7-block>
    <f7-block>
        <f7-list>
            <f7-list-item class="d-block"><b>Temàtica:</b> {{agenda.tematica}}</f7-list-item>
        </f7-list>
    </f7-block>
  </f7-page>
</template>

<style>
    .d-block .item-inner {
        display: block;
    }
</style>

<script>
  export default {
    data: function () {
      return {
        agenda: {
            titol: 'Mataró, un passeig per la història',
            descripcio: 'Descobreix Mataró fent un tast per la seva història a través d’anècdotes i lectures tot passejant pels carrers, edificis i places i gaudint dels racons més singulars.',
            tematica: 'Visita guiada',
            data: 'Dissabte 9 de febrer de 2019'
        },
      };
    }
  };
</script>
