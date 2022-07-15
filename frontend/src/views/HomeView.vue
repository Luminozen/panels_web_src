<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <button @click="getBoardList">Получить список панелей</button>
    <textarea>{{data}}</textarea>
  </div>
</template>

<script setup>
/* eslint-disable */
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import {ref} from 'vue'
import {getItem, addItem} from '@/api/modules/board'

let data = ref([])

async function getBoardList() {
  params = {board_id:null}
  data = await getItem(params)
}


</script>
