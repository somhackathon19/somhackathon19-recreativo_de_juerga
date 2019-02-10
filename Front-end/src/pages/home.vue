<style scoped>
  .page {
    background: url(/static/img/laia_arquera.jpeg) no-repeat;
    background-size: auto 100%;
  }

  .button {
    font-size: 20px;
    height: 150px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .buttons-block {
    margin-top: 25%;
  }

  .buttons-block .row2 {
    margin-top: 20px;
  }
</style>

<template>
  <f7-page name="home">
    <!-- Top Navbar -->
    <f7-navbar :sliding="false">
      <f7-nav-left>
        <f7-link icon-ios="f7:menu" icon-md="material:menu" panel-open="left"></f7-link>
      </f7-nav-left>
      <f7-nav-title>MATCONN</f7-nav-title>
    </f7-navbar>

    <f7-block class="buttons-block">
      <f7-row>
        <f7-col width="50">
          <f7-button href="/ajuntament/" fill raised large icon-material="today" icon-size="50px">Ajuntament</f7-button>
        </f7-col>
        <f7-col width="50">
          <f7-button href="/esports/" fill raised large icon-material="directions_bike" icon-size="50px">Esports</f7-button>
        </f7-col>
      </f7-row>
      <f7-row class="row2">
        <f7-col width="50">
          <f7-button href="/clubs/" fill raised large icon-material="group" icon-size="50px">Clubs</f7-button>
        </f7-col>
        <f7-col width="50">
          <f7-button href="/esdeveniments/" fill raised large icon-material="event_note" icon-size="50px">Esdeveniments</f7-button>
        </f7-col>
      </f7-row>
    </f7-block>
  </f7-page> 
</template>