<template>
  <div id="app">
    <Calendar />
  </div>
</template>

<script>
<<<<<<< HEAD
import Calendar from '../views/Calendar.vue';
import Login from '../views/login.vue';
=======
import Calendar from './components/Calendar.vue';
>>>>>>> parent of da9e3a4 (front変更)

export default {
  name: 'App',
  components: {
    Calendar,
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
