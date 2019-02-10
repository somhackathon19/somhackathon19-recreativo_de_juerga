<template>
  <f7-page name="contacte-ajuntament">
    <f7-navbar title="Contacte" back-link="Enrere"></f7-navbar>
        <f7-list inline-labels no-hairlines-md>
            <f7-list-input
                label="Nom"
                type="text"
                required
                clear-button
            >
            </f7-list-input>

            <f7-list-input
                label="Email"
                type="email"
                required
                clear-button
            >
            </f7-list-input>

            <f7-list-input
                type="textarea"
                placeholder="Escriu el teu missatge"
                required
                clear-button
            >
            </f7-list-input>

            <f7-list-button class="button-contacte">
                Enviar
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