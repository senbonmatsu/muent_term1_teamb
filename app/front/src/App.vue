<template>
  <div id="app">
    <template v-if="loggedIn">
      <Calendar />
    </template>
    <template v-else>
      <Login @login="handleLogin" />
    </template>
  </div>
</template>

<script>
import Calendar from '../views/Calendar.vue';
import Login from '../views/Login.vue';

export default {
  name: 'App',
  components: {
    Calendar,
    Login,
  },
  data() {
    return {
      loggedIn: false,
    };
  },
  methods: {
    handleLogin() {
      this.loggedIn = true;
    },
  },
};
</script>

<style>
/* スタイルをここに追加する */
</style>
