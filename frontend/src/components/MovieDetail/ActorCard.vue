<template>
  <div class="actor-card">
    <div class="card-image">
      <img :src="'//image.tmdb.org/t/p/w138_and_h175_face/' + actor.profile_path"> 
    </div>
    <div class="actor-content">
      <h2> {{ actor.ko_name }} </h2>
    </div>
  </div>
</template>

<script>
import "@/assets/css/components/movieDetail/actorCard.scss";
export default {
  name: "ActorCard",
  props: {
    actor: {
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