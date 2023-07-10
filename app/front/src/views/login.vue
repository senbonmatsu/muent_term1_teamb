<template>
    <div v-if="loggedIn">
      <Calendar />
    </div>
    <div v-else class="notebook">
      <!-- ログインフォームを表示 -->
      <h1>ログイン</h1>
      <input v-model="username_form" placeholder="ユーザー名" />
      <input v-model="password_form" type="password" placeholder="パスワード" />
      <button type="button" @click="login" class="login-button">ログイン</button>
      <button type="button" @click="goToSignup" class="signup-button">新規登録</button>
      <p v-if="message" class="message">{{ message }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import Calendar from '../views/Calendar.vue';
  
  export default {
    data() {
      return {
        username_form: '',
        password_form: '',
        message: '',
        loggedIn: false, // ログイン状態を追加
      };
    },
    methods: {
      // login() {
      //   axios
      //     .post('/user/login', {
      //       name: this.username_form,
      //       password: this.password_form,
      //     })
      //     .then((res) => {
      //       console.log(res.data);
      //       this.message = 'ログインに成功しました。';
      //       // ログイン成功時に認証情報を保存する
      //       localStorage.setItem('token', res.data.token);
      //       localStorage.setItem('user', JSON.stringify(res.data.user));
      //       this.loggedIn = true; // ログイン状態を更新
      //       // ログイン成功後の処理を追加
      //       window.location.reload(); // ページをリロード
      //     })
      //     .catch((err) => {
      //       console.log(err);
      //       this.message = 'ログインに失敗しました。';
      //     });
      // },

        login() {
            // ログイン成功のダミーレスポンスを設定
            const dummyResponse = {
                id: 1,
                username: 'ユーザー名',
            };

            this.message = 'ログインに成功しました。';
            this.loggedIn = true;
            localStorage.setItem('token', res.data.token);
            localStorage.setItem('user', JSON.stringify(res.data.user));
            window.location.reload(); // ページをリロード
            this.$router.push('/calendar'); // Vue Router を使用してページ遷移

            // または、コンポーネントをダイナミックに表示する場合
            // this.$emit('loginSuccess', dummyResponse); // イベントを発火して親コンポーネントで処理する
        },
        goToSignup() {
            this.$router.push('/signup'); // Vue Router を使用してページ遷移
        },

    },
    components: {
      Calendar,
    },
  };
  </script>
  
  <style scoped>

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
  button.login-button {
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
  button.signup-button {
    width: 100%;
    padding: 10px;
    background-color: transparent;
    border: none;
    cursor: pointer;
    }
  </style>
  