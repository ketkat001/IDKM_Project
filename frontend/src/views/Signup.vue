<template>
  <div class="signup-page">
    <div class="signup-box">
      <h2>우리 사이트에 처음 오셨군요!</h2>
      <div class="input-box">
        <label for="signup-id"> 아이디</label>
        <input
          type="text"
          v-model="signupData.userid"
          name="signup-id"
          placeholder="아이디를 입력하세요"
          required="아이디를 입력해 주세요."
        />
      </div>
      <div class="input-box">
        <label for="signup-password">비밀번호</label>
        <input
          type="password"
          v-model="signupData.password"
          name="signup-password"
          placeholder="비밀번호를 입력하세요"
          required="비밀번호를 입력해 주세요."
        />
      </div>
      <div class="input-box">
        <label for="signup-password-again"
          >비밀번호 확인
          <span v-show="!isPasswordMatch" class="warning-message"
            >비밀번호가 일치하지 않습니다!</span
          ></label
        >
        <input
          type="password"
          v-model.lazy="passwordCheck"
          name="signup-password-again"
          placeholder="비밀번호를 한번 더 입력하세요"
          required="비밀번호를 한번 더 입력하셔야 합니다."
        />
      </div>
      <div class="input-box">
        <label for="signup-username">이름</label>
        <input
          type="text"
          v-model="signupData.username"
          name="signup-username"
          placeholder="이름을 입력하세요"
          required="이메일을 입력해 주세요."
        />
      </div>
      <div class="input-box">
        <label for="signup-email">이메일</label>
        <input
          type="email"
          v-model="signupData.email"
          name="signup-email"
          placeholder="이메일 주소를 입력하세요"
          required="이메일을 입력해 주세요."
        />
      </div>

      <div class="submit-box">
        <input type="submit" value="회원 가입" :disabled="!hasAllProperty" @click="signup(signupData)"/>
        <span v-show="!hasAllProperty" class="warning-message">모든 정보를 입력해주세요!</span>
      </div>
    </div>
  </div>
</template>

<script>
import "@/assets/css/views/signup.scss";
import { mapActions } from "vuex"

export default {
  name: "Signup",
  created() {
    // email, id, password RegExp needed
  },
  computed: {
    isPasswordMatch() {
      return Boolean(
        this.passwordCheck !== '' &&
        this.signupData.password !== '' &&
        this.passwordCheck === this.signupData.password
      );
    },
    hasAllProperty() {
      return Boolean(
        this.signupData.userid !== '' && 
        this.signupData.username !== '' && 
        this.signupData.password !== '' && 
        this.signupData.email !== '' &&
        this.isPasswordMatch
      )
    }
  },
  methods: {
    ...mapActions(["signup"])
  },
  data() {
    return {
      passwordCheck: "",
      signupData: {
        userid: "",
        username: "",
        password: "",
        email: "",
      },
    };
  },
};
</script>
