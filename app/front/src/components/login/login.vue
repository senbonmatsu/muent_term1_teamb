<template>
    <div class="login">
      <h2>Login</h2>
      <form @submit="login">
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required>
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      async login() {
        try {
          const response = await fetch('/user/signup', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              name: this.username,
              password: this.password,
            }),
          });
  
          if (response.ok) {
            // Login successful, redirect to the calendar page
            this.$router.push('/calendar');
          } else {
            // Login failed, handle error
            const data = await response.json();
            console.log('Login failed:', data.detail);
          }
        } catch (error) {
          console.error('An error occurred during login:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .login {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  form {
    display: flex;
    flex-direction: column;
  }
  
  label {
    margin-bottom: 5px;
  }
  
  input {
    padding: 5px;
    margin-bottom: 10px;
  }
  
  button {
    padding: 10px;
    background-color: #2196f3;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  </style>
  