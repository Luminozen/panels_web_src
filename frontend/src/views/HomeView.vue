
<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <button @click="getBoardList">Получить список панелей</button>
    <p>{{data}}</p>
  </div>
</template>

<script setup>
// @ is an alias to /src
/* eslint-disable */
import HelloWorld from '@/components/HelloWorld.vue'
import {ref} from 'vue'
import {getBoard, addBoard, updateBoard, removeBoard} from '@/api/modules/board'

let data = ref([])


</script>
