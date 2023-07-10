<template>
  <div v-if="loggedIn">
    <Calendar />
  </div>
  <div v-else class="notebook">
    <!-- ログインフォームを表示 -->
    <h1>新規登録</h1>
    <input v-model="username_form" placeholder="新規ユーザー名" />
    <input v-model="password_form" type="password" placeholder="新規パスワード" />
    <button type="button" @click="sign_up">新規登録</button>
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
  //   sign_up() {
      //   axios
      //     .post('/user/signup', {
      //       name: this.username_form,
      //       password: this.password_form
      //     })
      //     .then(res => {
      //       console.log(res.data);
      //       this.message = '新規登録に成功しました。';
      //       this.loggedIn = true; // ログイン状態を更新
      //       // 新規登録成功後の処理を追加
      //       this.$router.push('/calendar'); // Vue Routerを使用してページ遷移
      //     })
      //     .catch(err => {
      //       console.log(err);
      //       this.message = '新規登録に失敗しました。';
      //     });
      // },

        sign_up() {
          // ログイン成功のダミーレスポンスを設定
          const dummyResponse = {
              id: 1,
              username: 'ユーザー名',
          };

          this.message = 'ログインに成功しました。';
          this.loggedIn = true;
          // ログイン後の処理
          // ここで必要なデータを取得したり、リダイレクトしたりする

          // 例えば、ログイン成功後に views/Calendar.vue を表示する場合
          this.$router.push('/calendar'); // Vue Router を使用してページ遷移

          // または、コンポーネントをダイナミックに表示する場合
          // this.$emit('loginSuccess', dummyResponse); // イベントを発火して親コンポーネントで処理する
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
