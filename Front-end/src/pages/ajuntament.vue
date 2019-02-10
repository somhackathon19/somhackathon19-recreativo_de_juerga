<template>
  <f7-page name="ajuntament">
    <f7-navbar title="Ajuntament" back-link="Enrere"></f7-navbar>
    <f7-block strong>
      Pàgina informativa d'esdeveniments, anuncis i notícies sobre la ciutat conectada directament a l'Ajuntament de Mataró
    </f7-block>
    <f7-list>
      <f7-list-button class="ajuntament-list-button" link="/agenda-cultural/"><f7-icon material="today"></f7-icon>&nbsp; Agenda cultural</f7-list-button>
    </f7-list>
    <f7-list>
      <f7-list-button class="ajuntament-list-button" link="/avisos/"><f7-icon material="info"></f7-icon>&nbsp; Avisos i notícies</f7-list-button>
    </f7-list>
    <f7-list>
      <f7-list-button class="ajuntament-list-button" link="/contacte-ajuntament/"><f7-icon material="contact_mail"></f7-icon>&nbsp; Contacte</f7-list-button>
    </f7-list>
  </f7-page>
</template>

<style scoped>
  li {
    height: 100px;
  }
  i {
    font-size: 60px;
  }
</style>