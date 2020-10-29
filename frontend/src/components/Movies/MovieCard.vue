<template>
  <v-card class="mx-auto" max-width="344">
    <v-img
      src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
      height="200px"
      width="250px"
    ></v-img>
    <v-card-title> {{ card.title }} </v-card-title>
    <v-card-subtitle> {{card.text}} content </v-card-subtitle>
    <v-card-actions>
      <v-btn color="orange lighten-2" text> Explore </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "MoviesCard",
  props: {
    card: {
      type: Object
    },
  }
}
</script>