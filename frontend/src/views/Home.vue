<template>
  <div class="home-content">
    <div class="main-search d-flex flex-column">
      <div class="home-logo">
        <a class="logo-homepage" href=""></a>
        <div class="home-search">
          <v-text-field
            class="search-input"
            name="input"
            label="생각나는 영화의 내용을 적어주세요"
            append-icon="mdi-magnify"
            :rules="rules">
          </v-text-field>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import "@/assets/css/components/home.scss";

export default {
  name: 'Home',
  data() {
    return {
      cards: []
    }
  }
}
</script>
