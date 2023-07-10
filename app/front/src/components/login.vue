<template>
    <input v-model='username_form'>
    <input v-model='password_form'>
    <button type="button" @click="login">送信</button>
    <p>{{message}}</p>
</template>
<script>
import axios from 'axios'
export default {
    data() {
        return {
            message: "",
        };
    },
    methods: {
        login: function () {
            axios
            .post("/user/login", {
                name: this.username_form,
                password: this.password_form,
            })
            .then((res) => {
                console.log(res.data);
            })
            .catch((err) => {
                console.log(err);
            });
        },
        }

    };

</script>
