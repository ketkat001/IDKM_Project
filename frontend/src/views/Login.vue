<template>
  <div class="login-page">
    <div class="login-box">
      <h1>로그인</h1>
      <div class="input-box">
        <label for="login-id">아이디</label>
        <input
          type="text"
          v-model.trim="loginData.email"
          name="login-id"
          placeholder="아이디를 입력하세요"
          required="아이디를 입력해 주세요."
        />
      </div>
      <div class="input-box">
        <label for="login-password">비밀번호</label>
        <input
          type="password"
          v-model.trim="loginData.password"
          name="login-password"
          placeholder="비밀번호를 입력하세요"
          required="비밀번호를 입력해 주세요."
          @keypress.enter="login(loginData)"
        />
      </div>
      <div class="submit-box">
        <input
          type="submit"
          value="로그인하기"
          :disabled="!hasAllProperties"
          @click="login(loginData)"
        />
        <span v-show="!hasAllProperties" class="warning-message"
          >아이디 또는 비밀번호를 입력해주세요!</span
        >
      </div>
      <p>
        <span
          >아직 회원이 아니신가요? <a href="/signup">회원가입 하러가기</a></span
        >
      </p>
    </div>
  </div>
</template>

<script>
import "@/assets/css/views/login.scss";
import { mapActions } from "vuex";

export default {
  name: "Login",
  computed: {
    hasAllProperties() {
      return !!this.loginData.email && !!this.loginData.password
    }
  },
  methods: {
    ...mapActions("accounts", ["login"]),
  },
  data() {
    return {
      loginData: {
        email: "",
        password: "",
      },
    };
  },
};
</script>

<style>
</style>