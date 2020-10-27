<template>
  <div class="home">
    <p>
      <span>This is Home.vue</span>
    </p>
    <input type="text" placeholder="검색어를 입력하세요!">
    <div>
      <h5>cards here</h5>
      
    </div>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      cards: []
    }
  }
}
</script>
