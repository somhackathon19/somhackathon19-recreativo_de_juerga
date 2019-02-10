<template>
  <f7-page name="esdeveniments">
    <f7-navbar title="Esdeveniments" back-link="Enrere">
        <f7-nav-right>
            <f7-button class="filter-button" icon-material="filter_list">&nbsp; Filtrar</f7-button>
        </f7-nav-right>
    </f7-navbar>
    <f7-list>
        <f7-list-button href="/afegir-esdeveniment/"><f7-icon material="add_circle_outline"></f7-icon>&nbsp; Afegir esdeveniment</f7-list-button>
    </f7-list>
    <f7-block>
        <f7-link v-for="esdeveniment in esdeveniments" :key="esdeveniment.id" no-link-class :href="`/esdeveniment/${esdeveniment.id}/`" class="card-link">
            <f7-card>
                <f7-card-header>
                    <div class="esdeveniment-header">
                        <h3>{{ esdeveniment.titol }}</h3>
                        <span>{{ $root.fixDate(esdeveniment.data_event) }} - {{ esdeveniment.hora }}</span>
                    </div>
                </f7-card-header>
                <f7-card-content>
                    {{ esdeveniment.descripcio }}
                </f7-card-content>
                <f7-card-footer>
                    <div class="esdeveniment-footer">
                        <span><f7-icon material="location_on"></f7-icon>Sant Simó</span>
                        <span class="full-flex"><b>Temàtica:</b> {{ esdeveniment.altres_tematica_especifica }}</span>
                    </div>
                </f7-card-footer>
            </f7-card>
        </f7-link>
    </f7-block>
  </f7-page>
</template>

<style>
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
</style>

<script>
export default {
    data() {
        return {
            esdeveniments: [
                {}
            ]
        }
    },

    created() {
        fetch('http://157.230.45.171:5000/api/esdeveniment/altres', {
            method: 'GET'
        })
        .then(response => {
            return response.json();
        })
        .then(data => {
            this.esdeveniments = data;
        })
    }
}
</script>