<template>
  <f7-page name="esports">
    <f7-navbar title="Esports" back-link="Enrere">
        <f7-nav-right>
            <f7-button class="filter-button" icon-material="filter_list">&nbsp; Filtrar</f7-button>
        </f7-nav-right>
    </f7-navbar>
    <f7-list>
        <f7-list-button href="/afegir-esport/"><f7-icon material="add_circle_outline"></f7-icon>&nbsp; Afegir esdeveniment esportiu</f7-list-button>
    </f7-list>
    <f7-block>
        <f7-link v-for="esport in esports" :key="esport.id" no-link-class :href="`/esport/${esport.id}/`" class="card-link">
            <f7-card>
                <f7-card-header>
                    <div class="esport-header">
                        <h3>{{ esport.titol }}</h3>
                        <span>{{ esport.data_event }}</span>
                    </div>
                </f7-card-header>
                <f7-card-content>
                    {{ esport.descripcio }}
                </f7-card-content>
                <f7-card-footer>
                    <div class="esport-footer">
                        <span>{{ esport.hora }}</span>
                        <span><f7-icon material="location_on"></f7-icon>Pla d'en boet</span>
                        <span>{{ esport.esport_rang }} ({{ esport.esport_participants }})</span>
                    </div>
                </f7-card-footer>
            </f7-card>
        </f7-link>

        <f7-link no-link-class :href="`/esport/${2}/`" class="card-link">
            <f7-card>
                <f7-card-header>
                    <div class="esport-header">
                        <h3>Ruta en bici 100km</h3>
                        <span>12/02/2019</span>
                    </div>
                </f7-card-header>
                <f7-card-content>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus rutrum commodo turpis ut pellentesque. Nunc fermentum cursus purus at maximus. Donec eget felis et augue mattis tempus. Vestibulum eleifend varius lacinia.
                </f7-card-content>
                <f7-card-footer>
                    <div class="esport-footer">
                        <span>8:00</span>
                        <span><f7-icon material="location_on"></f7-icon>Sant Simó</span>
                        <span>Ilimitat (28)</span>
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
</style>

<script>
export default {
    data() {
        return {
            esports: [
                {}
            ]
        }
    },

    created() {
        fetch('http://157.230.45.171:5000/api/esdeveniment/esport', {
            method: 'GET'
        })
        .then(response => {
            return response.json();
        })
        .then(data => {
            this.esports = data;
        })
    }
}
</script>