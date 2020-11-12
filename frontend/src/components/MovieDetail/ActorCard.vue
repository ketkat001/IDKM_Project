<template>
  <div class="actor-card">
    <div class="card-image">
      <img src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"> 
    </div>
    <div class="actor-content">
      <h2> {{ card.title }} </h2>
    </div>
  </div>
</template>

<script>
import "@/assets/css/components/movieDetail/actorCard.scss";
export default {
  name: "ActorCard",
  props: {
    card: {
      type: Object
    },
  },
  data () {
    return {
    }
  }
}
</script>

<style>

</style>