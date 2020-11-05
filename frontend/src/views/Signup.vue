<template>
  <div class="signup-page">
    <div class="signup-box">
      <h2>우리 사이트에 처음 오셨군요!</h2>
      <div class="input-box">
        <label for="signup-email"
          >이메일<span v-show="!isEmailEmpty" class="warning-message"
            >이메일을 입력해주세요!!</span
          ></label
        >
        <input
          type="email"
          v-model="signupData.email"
          name="signup-email"
          placeholder="이메일 주소를 입력하세요"
          required="이메일을 입력해 주세요."
          @focus="emailFlag = true"
        />
      </div>
      <div class="input-box">
        <label for="signup-password"
          >비밀번호
          <span v-show="!isPasswordMatch" class="warning-message"
            >비밀번호를 입력해 주세요!</span
          >
        </label>
        <input
          type="password"
          v-model.lazy.trim="signupData.password"
          name="signup-password"
          placeholder="비밀번호를 입력하세요"
          @focus="passwordFlag = true"
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
          v-model.trim="passwordCheck"
          name="signup-password-again"
          placeholder="비밀번호를 한번 더 입력하세요"
          required="비밀번호를 한번 더 입력하셔야 합니다."
        />
      </div>
      <div class="input-box">
        <label for="signup-username"
          >이름<span v-show="!isUsernameEmpty" class="warning-message"
            >이름을 입력해 주세요!</span
          ></label
        >
        <input
          type="text"
          v-model="signupData.username"
          name="signup-username"
          placeholder="이름을 입력하세요"
          required="이메일을 입력해 주세요."
          @focus="usernameFlag = true"
        />
      </div>

      <div class="submit-box">
        <input
          type="submit"
          value="회원 가입"
          :disabled="!hasAllProperty"
          @click="signup(signupData)"
        />
        <span v-show="!hasAllProperty" class="warning-message"
          >모든 정보를 입력해주세요!</span
        >
      </div>
    </div>
  </div>
</template>

<script>
import "@/assets/css/views/signup.scss";
import { mapActions } from "vuex";

export default {
  name: "Signup",
  created() {
    // email, id, password RegExp needed
  },
  computed: {
    isEmailEmpty() {
      return this.emailFlag && !!this.signupData.email;
    },
    isUsernameEmpty() {
      return this.usernameFlag && !!this.signupData.username;
    },
    isPasswordEmpty() {
      return !this.signupData.password;
    },
    isPasswordMatch() {
      return this.passwordCheck === this.signupData.password;
    },
    hasAllProperty() {
      return Boolean(
        this.signupData.username !== "" &&
          this.signupData.password !== "" &&
          this.signupData.email !== "" &&
          this.isPasswordMatch
      );
    },
  },
  methods: {
    ...mapActions("accounts", ["signup"]),
  },
  data() {
    return {
      emailFlag: false,
      passwordFlag: false,
      usernameFlag: false,
      passwordCheck: "",
      signupData: {
        username: "",
        password: "",
        email: "",
      },
    };
  },
};
</script>
