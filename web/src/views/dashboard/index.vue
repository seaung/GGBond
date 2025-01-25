<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'

// 统计数据
interface DashboardStats {
  deviceCount: number
  vulnCount: number
  taskCount: number
  recentScans: Array<{
    id: number
    name: string
    status: string
    time: string
  }>
}

const loading = ref(true)
const stats = ref<DashboardStats>({
  deviceCount: 0,
  vulnCount: 0,
  taskCount: 0,
  recentScans: []
})

// 模拟获取数据
const fetchDashboardData = async () => {
  try {
    // TODO: 替换为实际的API调用
    await new Promise(resolve => setTimeout(resolve, 1000))
    stats.value = {
      deviceCount: 128,
      vulnCount: 56,
      taskCount: 23,
      recentScans: [
        { id: 1, name: '安全扫描-A区', status: '完成', time: '2024-01-20 10:30' },
        { id: 2, name: '安全扫描-B区', status: '进行中', time: '2024-01-20 09:15' },
        { id: 3, name: '安全扫描-C区', status: '等待中', time: '2024-01-20 08:45' }
      ]
    }
  } catch (error) {
    ElMessage.error('获取数据失败')
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchDashboardData()
})
</script>

<template>
  <div class="dashboard-container">
    <el-row :gutter="20">
      <!-- 统计卡片 -->
      <el-col :span="8">
        <el-card shadow="hover" class="stat-card">
          <template #header>
            <div class="card-header">
              <span>设备总数</span>
            </div>
          </template>
          <div v-loading="loading" class="stat-value">
            {{ stats.deviceCount }}
          </div>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="hover" class="stat-card">
          <template #header>
            <div class="card-header">
              <span>漏洞总数</span>
            </div>
          </template>
          <div v-loading="loading" class="stat-value">
            {{ stats.vulnCount }}
          </div>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="hover" class="stat-card">
          <template #header>
            <div class="card-header">
              <span>扫描任务</span>
            </div>
          </template>
          <div v-loading="loading" class="stat-value">
            {{ stats.taskCount }}
          </div>
        </el-card>
      </el-col>
    </el-row>

    <!-- 最近扫描任务 -->
    <el-card class="recent-scans" style="margin-top: 20px">
      <template #header>
        <div class="card-header">
          <span>最近扫描任务</span>
        </div>
      </template>
      <el-table v-loading="loading" :data="stats.recentScans" style="width: 100%">
        <el-table-column prop="name" label="任务名称" />
        <el-table-column prop="status" label="状态">
          <template #default="{ row }">
            <el-tag :type="row.status === '完成' ? 'success' : row.status === '进行中' ? 'primary' : 'info'">
              {{ row.status }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="time" label="时间" width="180" />
      </el-table>
    </el-card>
  </div>
</template>

<style scoped>
.dashboard-container {
  padding: 20px;
}

.stat-card {
  height: 180px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.stat-value {
  font-size: 36px;
  font-weight: bold;
  text-align: center;
  margin-top: 20px;
}
</style>