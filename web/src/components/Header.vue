<script setup lang="ts">
import { useUserStore } from '../store/user'
import { useRouter } from 'vue-router'

const props = defineProps<{
  isCollapse: boolean
}>()

const emit = defineEmits<{
  'toggle-sidebar': []
}>()

const userStore = useUserStore()
const router = useRouter()

const handleLogout = () => {
  userStore.logout()
  router.push('/login')
}

const toggleSidebar = () => {
  emit('toggle-sidebar')
}
</script>

<template>
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
</template>

<style lang="scss" scoped>
.header {
  background-color: #fff;
  border-bottom: 1px solid #e6e6e6;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;

  :global(.toggle-button) {
    font-size: 24px;
    cursor: pointer;
    color: #1a1a1a;
    transition: all 0.3s ease;
    padding: 8px;
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;

    &:hover {
      color: #409EFF;
      background-color: #f5f7fa;
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
</style>