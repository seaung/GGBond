<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps<{
  isCollapse: boolean
}>()
</script>

<template>
  <el-aside :width="isCollapse ? '64px' : '200px'" class="sidebar">
    <div class="logo-container">
      <img src="/vite.svg" alt="Logo" class="logo" />
      <span v-show="!isCollapse" class="title">GGBond</span>
    </div>
    <el-menu
      :collapse="isCollapse"
      :collapse-transition="false"
      :router="true"
      class="sidebar-menu"
      background-color="#304156"
      text-color="#bfcbd9"
      active-text-color="#409EFF"
    >
      <el-menu-item index="/dashboard">
        <el-icon><Monitor /></el-icon>
        <template #title>仪表盘</template>
      </el-menu-item>
      <el-menu-item index="/devices">
        <el-icon><Connection /></el-icon>
        <template #title>设备管理</template>
      </el-menu-item>
      <el-menu-item index="/vulnerabilities">
        <el-icon><Warning /></el-icon>
        <template #title>漏洞扫描</template>
      </el-menu-item>
      <el-menu-item index="/tasks">
        <el-icon><List /></el-icon>
        <template #title>任务管理</template>
      </el-menu-item>
    </el-menu>
  </el-aside>
</template>

<style lang="scss" scoped>
.sidebar {
  transition: width 0.3s;
  background-color: #304156;

  .logo-container {
    height: 60px;
    display: flex;
    align-items: center;
    padding: 0 16px;
    background-color: #2b3649;

    .logo {
      width: 32px;
      height: 32px;
    }

    .title {
      margin-left: 12px;
      color: #fff;
      font-size: 16px;
      font-weight: 600;
    }
  }

  .sidebar-menu {
    border: none;
  }
}
</style>