<template>
  <div class="notebook">
    <h1>ログイン</h1>
    <input v-model="username_form" placeholder="ユーザー名" />
    <input v-model="password_form" type="password" placeholder="パスワード" />
    <button type="button" @click="login">ログイン</button>
    <p v-if="message" class="message">{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username_form: '',
      password_form: '',
      message: '',
    };
  },
  methods: {
    login() {
      axios
        .post('/user/login', {
          name: this.username_form,
          password: this.password_form,
        })
        .then((res) => {
          console.log(res.data);
          this.message = 'ログインに成功しました。';
        })
        .catch((err) => {
          console.log(err);
          this.message = 'ログインに失敗しました。';
        });
    },
  },
};
</script>

<style>
html {
    background-image: linear-gradient(#eee 1px, transparent 1px),
      linear-gradient(90deg, #eee 1px, transparent 1px);
    background-size: 3mm 3mm;
    background-position: -1px -1px;
}
body {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.notebook {
  max-width: 400px;
  padding: 20px;
  background-color: #f5f4f0;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
  font-size: 24px;
  margin-bottom: 20px;
}

input {
  width: 94%;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.message {
  text-align: center;
  margin-top: 10px;
}
</style>
