<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script setup>
/* eslint-disable */
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

import axios from 'axios'
import {ref} from 'vue'

let data = ref([])

const BASE_URL = axios.create(
  {
    baseURL: 'http://127.0.0.1:8000/api/',
    headers: {
      contentType: "application/json"
    }
  }
)

BASE_URL.get('boards/list/').then(response => {
  console.log(response);
  data.value = response.data
})


</script>
