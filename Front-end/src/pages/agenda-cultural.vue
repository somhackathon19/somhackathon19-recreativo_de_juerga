<template>
  <f7-page name="agenda-cultural">
    <f7-navbar title="Agenda cultural" back-link="Enrere"></f7-navbar>
        <f7-block>
            <f7-link no-link-class :href="`/agenda-cultural/${1}/`" class="card-link">
                <f7-card>
                    <f7-card-header
                        class="no-border agenda-header"
                        valign="bottom"
                        style="background-image:url(/static/img/cultural1.JPG)"
                    >Mataró, un passeig per la història</f7-card-header>
                    <f7-card-content>
                        <p class="date">Dissabte 9 de febrer de 2019</p>
                        <p>Descobreix Mataró fent un tast per la seva història a través d’anècdotes i lectures tot passejant pels carrers, edificis i places i gaudint dels racons més singulars.</p>
                    </f7-card-content>
                    <f7-card-footer>
                        <div class="agenda-footer">
                            <span><f7-icon material="location_on"></f7-icon>Ajuntament de mataró</span>
                            <span class="full-flex"><b>Temàtica:</b> Visita guiada</span>
                        </div>
                    </f7-card-footer>
                </f7-card>
            </f7-link>

            <f7-link no-link-class :href="`/agenda-cultural/${2}/`" class="card-link">
                <f7-card>
                    <f7-card-header
                        class="no-border agenda-header"
                        valign="bottom"
                        style="background-image:url(/static/img/cultural2.jpg)"
                    >Vil·la romana de Torre Llauder</f7-card-header>
                    <f7-card-content>
                        <p class="date">Dissabte 9 de febrer de 2019</p>
                        <p>
                      Visita guiada al jaciment arqueològic de Torre Llauder. Veurem com era la vil·la romana que s'ha conservat i passejarem per les dependències decorades amb esplèndids mosaics de colors, els ...</p>
                    </f7-card-content>
                    <f7-card-footer>
                        <div class="agenda-footer">
                            <span><f7-icon material="location_on"></f7-icon>Vil·la romana de Torre Llauder</span>
                            <span class="full-flex"><b>Temàtica:</b> Visita guiada</span>
                        </div>
                    </f7-card-footer>
                </f7-card>
            </f7-link>

            <f7-link no-link-class :href="`/agenda-cultural/${3}/`" class="card-link">
                <f7-card>
                    <f7-card-header
                        class="no-border agenda-header"
                        valign="bottom"
                        style="background-image:url(/static/img/cultural3.jpg)"
                    >Rosa Codina-Esteve. Vacuum</f7-card-header>
                    <f7-card-content>
                        <p class="date">Dissabte 9 de febrer de 2019</p>
                        <p>Rosa Codina-Esteve (Mataró, 1948) presenta la seva obra més recent a la mostra “Vacuum”, una trentena de pintures de gran format que ens mostren la multiplicitat d’uns objectes ...</p>
                    </f7-card-content>
                    <f7-card-footer>
                        <div class="agenda-footer">
                            <span><f7-icon material="location_on"></f7-icon>Ca l’Arenas Centre d’Art. Museu de Mataró</span>
                            <span class="full-flex"><b>Temàtica:</b> Visita guiada</span>
                        </div>
                    </f7-card-footer>
                </f7-card>
            </f7-link>
        </f7-block>
  </f7-page>
</template>

<style>
    .agenda-header {
        height: 100px;
        color: white;
        text-shadow: 2px 2px 4px #000;
    }
    
    .agenda-footer{
        width: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
    }

    .agenda-footer span {
        flex: 1;
        text-align: center;
    }
</style>