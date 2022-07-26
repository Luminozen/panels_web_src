<template>
  <div class="default-layout">
    <el-container>
      <el-drawer ref="sidebarDrawer" v-model="sidebar"
        direction="ltr" custom-class="sidebar"></el-drawer>
      <el-container>
        <el-header>
          <el-button type="primary" @click="sidebar = true">Открыть сайдбар</el-button>
        </el-header>
        <el-main>
          <!-- Попробуйте закомментить эту строку -->
          <slot></slot>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import {ref} from 'vue'
// Переменная отвечающая за состояние видимости сайдбара
const sidebar = ref(false)
const sidebarDrawer = ref(null)

</script>

<style lang="scss">
.default-layout {
  .sidebar {
    width: 20% !important;
    // background-color: black;
  }
}
</style>
