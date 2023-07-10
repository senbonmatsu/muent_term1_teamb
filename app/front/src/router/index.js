import { createRouter, createWebHistory } from 'vue-router';
import Vue from 'vue';
import App from './App.vue';

const routes = [
  {
    path: '/',
    name: 'signup',
    component: () => import(/* webpackChunkName: "about" */ '../views/signup.vue')
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
