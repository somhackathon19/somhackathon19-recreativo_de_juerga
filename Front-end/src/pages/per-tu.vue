<template>
  <f7-page name="per-tu">
    <f7-navbar>
        <f7-nav-left>
            <f7-link icon-ios="f7:menu" icon-md="material:menu" panel-open="left"></f7-link>
        </f7-nav-left>
        <f7-nav-title>
            Per tu
        </f7-nav-title>
        <f7-nav-right>
            <f7-button class="filter-button" icon-material="filter_list">&nbsp; Filtrar</f7-button>
        </f7-nav-right>
    </f7-navbar>
    <f7-block>
        <h3>Esports</h3>
        <f7-link no-link-class :href="`/esport/${1}/`" class="card-link">
            <f7-card>
                <f7-card-header>
                    <div class="esport-header">
                        <h3>Torneig de bàsquet 3x3</h3>
                        <span>11/02/2019</span>
                    </div>
                </f7-card-header>
                <f7-card-content>
                    Qui s'apunta a una patxanga el proper diumenge 1 de maig de 2019 a Pla d'en Boet?
                </f7-card-content>
                <f7-card-footer>
                    <div class="esport-footer">
                        <span>17:00</span>
                        <span><f7-icon material="location_on"></f7-icon>Pla d'en boet</span>
                        <span>10-30 (15)</span>
                    </div>
                </f7-card-footer>
            </f7-card>
        </f7-link>
    </f7-block>

    <f7-block>
        <h3>Esdeveniments</h3>
        <f7-link no-link-class :href="`/esdeveniment/${1}/`" class="card-link">
            <f7-card>
                <f7-card-header>
                    <div class="esdeveniment-header">
                        <h3>Mercat de dissabte</h3>
                        <span>11/02/2019 - 8:00</span>
                    </div>
                </f7-card-header>
                <f7-card-content>
                    Mercat a la Plaça de Cuba de fruita i verdura, quedarà tallada la Plaça durant tot el matí. 
                </f7-card-content>
                <f7-card-footer>
                    <div class="esdeveniment-footer">
                        <span><f7-icon material="location_on"></f7-icon>Plaça de Cuba</span>
                        <span class="full-flex"><b>Temàtica:</b> Fruita i verdura</span>
                    </div>
                </f7-card-footer>
            </f7-card>
        </f7-link>
    </f7-block>

    <f7-block>
        <h3>Clubs</h3>
        <f7-link no-link-class :href="`/club/${1}/`" class="card-link">
            <f7-card>
                <f7-card-header>
                    <div class="club-header">
                        <h3>Club d'Escacs (amateur)</h3>
                    </div>
                </f7-card-header>
                <f7-card-content>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus rutrum commodo turpis ut pellentesque. Nunc fermentum cursus purus at maximus. Donec eget felis et augue mattis tempus. Vestibulum eleifend varius lacinia.
                </f7-card-content>
                <f7-card-footer>
                    <div class="club-footer">
                        <span>65 membres</span>
                    </div>
                </f7-card-footer>
            </f7-card>
        </f7-link>
    </f7-block>
  </f7-page>
</template>

<style>
    .esport-header {
        width: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
    }

    .esport-header span {
        flex: 1;
        text-align: right;
    }
    .esport-footer{
        width: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
    }

    .esport-footer span {
        flex: 1;
        text-align: center;
    }
    .esdeveniment-header {
        width: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
    }

    .esdeveniment-header span {
        flex: 1;
        text-align: right;
    }
    .esdeveniment-footer{
        width: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
    }

    .esdeveniment-footer span {
        flex: 0.5;
        text-align: center;
    }

    span.full-flex {
        flex: 1;
    }

    .club-header {
        width: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
    }

    .club-header span {
        flex: 1;
        text-align: right;
    }
    .club-footer{
        width: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
    }

    .club-footer span {
        flex: 1;
        text-align: center;
    }
</style>