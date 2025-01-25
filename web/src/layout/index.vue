<script setup lang="ts">
import { ref } from 'vue'
import Sidebar from '../components/Sidebar.vue'
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'

const isCollapse = ref(false)

const handleToggleSidebar = () => {
  isCollapse.value = !isCollapse.value
}
</script>

<template>
  <el-container class="layout-container">
    <Sidebar :is-collapse="isCollapse" />
    <el-container>
      <Header :is-collapse="isCollapse" @toggle-sidebar="handleToggleSidebar" />
      <el-main class="main-content">
        <router-view />
      </el-main>
      <Footer />
    </el-container>
  </el-container>
</template>

<style lang="scss" scoped>
.layout-container {
  height: 100vh;
  display: flex;

  .el-container {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;

    .main-content {
      flex: 1;
      background-color: #f0f2f5;
      padding: 20px;
      overflow-y: auto;
    }
  }
}
</style>
