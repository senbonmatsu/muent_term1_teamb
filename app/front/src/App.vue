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
import Login from '../views/login.vue';

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
</style>
