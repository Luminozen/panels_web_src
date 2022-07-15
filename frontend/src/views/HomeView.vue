
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
import {getItem, addItem} from '@/api/modules/board'

let data = ref([])

async function getBoardList() {
  let params = {board_id:null}
  data.value = await getItem(params)
  console.log(data);
}


</script>
