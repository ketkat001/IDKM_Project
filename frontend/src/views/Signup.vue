<template>
  <div class="signup-page">
    <div class="signup-box">
      <h2>우리 사이트에 처음 오셨군요!</h2>
      <!-- email block -->
      <div class="input-box">
        <div class="validate-label">
          <div>
            <label for="signup-email">
              이메일<span v-show="!isEmailValid" class="warning-message"
                >이메일 형식이 올바르지 않습니다!</span
              >
            </label>
          </div>
          <div>
            <v-btn
              elevation="2"
              color="amber"
              :disabled="!emailFlag || !isEmailValid"
              @click="validateEmail"
              >이메일 인증</v-btn
            >
          </div>
        </div>
        <input
          type="email"
          v-model="signupData.email"
          name="signup-email"
          placeholder="이메일 주소를 입력하세요"
          required="이메일을 입력해 주세요."
          @focus="emailFlag = true"
        />
      </div>
      <!-- nickname block -->
      <div class="input-box">
        <div class="validate-label">
          <div>
            <label for="signup-nickname"
              >닉네임<span v-show="isNicknameEmpty" class="warning-message"
                >닉네임을 입력해주세요</span
              ></label
            >
          </div>
          <div>
            <v-btn
              elevation="2"
              color="amber"
              :disabled="!nicknameFlag || isNicknameEmpty"
              @click="validateNickname"
              >닉네임 인증</v-btn
            >
          </div>
        </div>

        <input
          type="text"
          v-model="signupData.nickname"
          name="signup-nickname"
          placeholder="홈페이지에서 사용될 닉네임을 입력하세요"
          required="네임을 입력해 주세요."
          @focus="nicknameFlag = true"
        />
      </div>
      <!-- password block -->
      <div class="input-box">
        <label for="signup-password"
          >비밀번호
          <span v-show="isPasswordEmpty" class="warning-message"
            >비밀번호를 입력해 주세요!</span
          >
        </label>
        <input
          type="password"
          v-model.trim="signupData.password"
          name="signup-password"
          placeholder="비밀번호를 입력하세요"
          @focus="passwordFlag = true"
          required="비밀번호를 입력해 주세요."
        />
      </div>
      <!-- password check block -->
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
      <!-- signup button -->
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
import axios from "axios";
import SERVER from "@/api/drf.js";
import "@/assets/css/views/signup.scss";
import { mapActions } from "vuex";

export default {
  name: "Signup",
  created() {
    // email, id, password RegExp needed
  },
  computed: {
    isEmailValid() {
      const email = this.signupData.email;
      const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return this.emailFlag ? pattern.test(email) : true;
    },
    isNicknameEmpty() {
      return this.nicknameFlag && !this.signupData.nickname;
    },
    isPasswordEmpty() {
      return this.passwordFlag && !this.signupData.password;
    },
    isPasswordMatch() {
      return this.passwordCheck === this.signupData.password;
    },
    hasAllProperty() {
      return (
        !this.isPasswordEmpty &&
        !this.isNicknameEmpty &&
        this.isPasswordMatch &&
        this.isEmailValid &&
        this.emailFlag &&
        this.passwordFlag &&
        this.nicknameFlag
      );
    },
  },
  methods: {
    ...mapActions("accounts", ["signup"]),
    validateEmail() {
      // console.log(email, "will be validated");
      const email = this.signupData.email;
      const URL = SERVER.URL + SERVER.R.ACCOUNTS.check;
      axios.post(URL, { "email": email })
        .then(res => {
          if (res === true) {
            alert("사용 가능한 이메일 입니다!")
          } else { 
            alert("오우.. 이미 누가 사용중인가봐요.. ㅜㅜ")
          }
        })
        .catch(err => console.log(err))
    },
    validateNickname() {
      // console.log(nickname, "will be validated");
      const nickname = this.signupData.nickname;
      const URL = SERVER.URL + SERVER.R.ACCOUNTS.check;
      axios.post(URL, { "nickname": nickname })
        .then(res => {
          if (res === true) {
            alert("사용 가능한 이메일 입니다!")
          } else { 
            alert("오우.. 이미 누가 사용중인가봐요.. ㅜㅜ")
          }
        })
        .catch(err => console.log(err))
    },
  },
  data() {
    return {
      emailFlag: false,
      passwordFlag: false,
      nicknameFlag: false,
      passwordCheck: "",
      signupData: {
        nickname: "",
        password: "",
        email: "",
      },
    };
  },
};
</script>
