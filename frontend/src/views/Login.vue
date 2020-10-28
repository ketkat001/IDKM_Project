<template>
  <div class="login-page">
    <div class="login-box">
      <h1>로그인</h1>
      <div class="input-box">
        <label for="login-id">아이디</label>
        <input
          type="text"
          label="id"
          name="login-id"
          placeholder="아이디를 입력하세요"
          required="아이디를 입력해 주세요."
        />
      </div>
      <div class="input-box">
        <label for="login-password">비밀번호</label>
        <input
          type="password"
          label="password"
          name="login-password"
          placeholder="비밀번호를 입력하세요"
          required="비밀번호를 입력해 주세요."
        />
      </div>
      <div class="submit-box">
        <input type="submit" value="로그인하기" />
        <span class="warning-message"
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
import "@/assets/css/login.scss";

export default {
  name: "Login",
  data() {
    return {
      loginData: {
        userid: "",
        password: "",
      },
    };
  },
};
</script>

<style>
</style>