<template>
  <div class="home">
    <button @click="getBoardList">Получить список панелей</button>
    <p>{{data}}</p>
  </div>
</template>

<script setup>
// @ is an alias to /src
/* eslint-disable */
import {ref} from 'vue'
import {getBoard, addBoard, updateBoard, removeBoard} from '@/api/modules/board'

let data = ref([])


</script>