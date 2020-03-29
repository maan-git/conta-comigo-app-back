<template>
  <v-app-bar
    app
    color="primary"
    dark
  >
    <div class="d-flex align-center">
      <v-img
        alt="Vuetify Logo"
        class="shrink mr-2 hidden-md-and-up"
        contain
        :src="require('../assets/icone.svg')"
        transition="scale-transition"
        width="40"
      />

      <v-img
        alt="Vuetify Name"
        class="shrink mt-1 hidden-sm-and-down"
        contain
        min-width="100"
        :src="require('../assets/logo_completa.svg')"
        width="100"
      />
    </div>

    <v-spacer></v-spacer>

    <v-btn to="/about" text>
      <span>about</span>
    </v-btn>
    <v-btn to="/login" text>
      <span>login</span>
    </v-btn>
    <v-btn to="/create-account" text>
      <span>create account</span>
    </v-btn>
    <v-btn to="/create-help" text>
      <span>create help</span>
    </v-btn>
  </v-app-bar>
</template>
