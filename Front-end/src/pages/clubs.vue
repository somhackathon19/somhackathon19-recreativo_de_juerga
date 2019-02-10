<template>
  <f7-page name="clubs">
    <f7-navbar title="Clubs" back-link="Enrere">
        <f7-nav-right>
            <f7-button class="filter-button" icon-material="filter_list">&nbsp; Filtrar</f7-button>
        </f7-nav-right>
    </f7-navbar>
    <f7-list>
        <f7-list-button href="/afegir-club/"><f7-icon material="add_circle_outline"></f7-icon>&nbsp; Afegir club</f7-list-button>
    </f7-list>

    <f7-block>
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

        <f7-link no-link-class :href="`/club/${2}/`" class="card-link">
            <f7-card>
                <f7-card-header>
                    <div class="club-header">
                        <h3>Els aventurers</h3>
                    </div>
                </f7-card-header>
                <f7-card-content>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus rutrum commodo turpis ut pellentesque. Nunc fermentum cursus purus at maximus. Donec eget felis et augue mattis tempus. Vestibulum eleifend varius lacinia.
                </f7-card-content>
                <f7-card-footer>
                    <div class="club-footer">
                        <span>14 membres</span>
                    </div>
                </f7-card-footer>
            </f7-card>
        </f7-link>
    </f7-block>
  </f7-page>
</template>

<style>
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

<script>
export default {
    data() {
        return {
            clubs: [
                {}
            ]
        }
    },

    created() {
        fetch('http://157.230.45.171:5000/api/esdeveniment/club', {
            method: 'GET'
        })
        .then(response => {
            return response.json();
        })
        .then(data => {
            this.clubs = data;
        })
    }
}
</script>