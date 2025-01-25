<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '../store/user'

const isCollapse = ref(false)
const userStore = useUserStore()
const router = useRouter()

const handleLogout = () => {
  userStore.logout()
  router.push('/login')
}

const toggleSidebar = () => {
  isCollapse.value = !isCollapse.value
}
</script>

<template>
  <el-container class="layout-container">
    <!-- 侧边栏 -->
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

    <el-container>
      <!-- 头部导航 -->
      <el-header class="header">
        <div class="header-left">
          <el-icon class="toggle-button" @click="toggleSidebar">
            <Fold v-if="!isCollapse" />
            <Expand v-else />
          </el-icon>
        </div>
        <div class="header-right">
          <el-dropdown trigger="click">
            <span class="user-info">
              <el-avatar :size="32" :src="userStore.userInfo.avatar || '/vite.svg'" />
              <span class="username">{{ userStore.userInfo.username }}</span>
            </span>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item @click="handleLogout">退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </el-header>

      <!-- 主要内容区域 -->
      <el-main class="main-content">
        <router-view />
      </el-main>

      <!-- 页脚 -->
      <el-footer class="footer">
        <div class="footer-content">
          © 2024 GGBond. All rights reserved.
        </div>
      </el-footer>
    </el-container>
  </el-container>
</template>

<style lang="scss" scoped>
.layout-container {
  height: 100vh;

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

  .header {
    background-color: #fff;
    border-bottom: 1px solid #e6e6e6;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 20px;

    .toggle-button {
      font-size: 20px;
      cursor: pointer;
      color: #333;
      transition: color 0.3s ease;

      &:hover {
        color: #409EFF;
      }
    }

    .user-info {
      display: flex;
      align-items: center;
      cursor: pointer;

      .username {
        margin-left: 8px;
        color: #606266;
      }
    }
  }

  .main-content {
    background-color: #f0f2f5;
    padding: 20px;
  }

  .footer {
    background-color: #fff;
    border-top: 1px solid #e6e6e6;
    display: flex;
    align-items: center;
    justify-content: center;

    .footer-content {
      color: #606266;
      font-size: 14px;
    }
  }
}
</style>
