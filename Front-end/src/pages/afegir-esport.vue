<template>
  <f7-page name="afegir-esport">
    <f7-navbar title="Afegir esport" back-link="Enrere"></f7-navbar>
        <f7-list inline-labels no-hairlines-md>
            <f7-list-input
                label="Títol"
                type="text"
                required
                clear-button
            >
            </f7-list-input>

            <f7-list-input
                type="textarea"
                placeholder="Descripció"
                required
                clear-button
            >
            </f7-list-input>

            <f7-list-input
                label="Data"
                type="text"
                required
                clear-button
            >
            </f7-list-input>

            <f7-list-input
                label="Hora"
                type="text"
                required
                clear-button
            >
            </f7-list-input>

            <f7-list-input
                label="Ubicació"
                type="text"
                required
                clear-button
            >
            </f7-list-input>

            <f7-list-input
                label="Nº participants"
                type="number"
                required
                clear-button
            >
            </f7-list-input>

            <f7-list-input
                label="Subcategoria 1"
                type="select"
                required
                clear-button
            >
            </f7-list-input>

            <f7-list-input
                label="Subcategoria 2"
                type="select"
                clear-button
            >
            </f7-list-input>

            <f7-list-input
                label="Subcategoria 3"
                type="select"
                clear-button
            >
                <option v-for="tag in $root.tags" :key="tag.id" :value="tag.id">{{ tag.nom }}</option>
            </f7-list-input>

            <f7-list-button class="button-contacte" @click="sendData()">
                Afegir
            </f7-list-button>
        </f7-list>
    </f7-page>
</template>

<style scoped>
    .button-contacte {
        background: #f5f5f5;
        display: flex;
        justify-content: center;
    }
</style>

<script>
export default {
    methods: {
        sendData() {

        }
    }
}
</script>