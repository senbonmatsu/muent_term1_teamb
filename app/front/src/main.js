import axios from 'axios';
import { createApp } from 'vue';
import App from './App.vue';


axios.defaults.withCredentials = true;
axios.defaults.headers.post['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8000';
axios.defaults.baseURL = 'http://127.0.0.1:8000';  // the FastAPI backend
createApp(App).mount('#app')
