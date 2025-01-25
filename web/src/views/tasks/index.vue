<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'

interface Task {
  id: number
  name: string
  type: string
  status: 'pending' | 'running' | 'completed' | 'failed'
  progress: number
  target: string
  startTime: string
  endTime: string
  description: string
}

const tasks = ref<Task[]>([])
const loading = ref(true)
const detailsDialogVisible = ref(false)
const selectedTask = ref<Task | null>(null)

const fetchTasks = async () => {
  try {
    // TODO: 替换为实际的API调用
    await new Promise(resolve => setTimeout(resolve, 1000))
    tasks.value = [
      {
        id: 1,
        name: '安全扫描任务-A区',
        type: '漏洞扫描',
        status: 'running',
        progress: 45,
        target: '192.168.1.100',
        startTime: '2024-01-20 15:30:00',
        endTime: '',
        description: 'A区服务器安全扫描'
      },
      {
        id: 2,
        name: '安全扫描任务-B区',
        type: '漏洞扫描',
        status: 'completed',
        progress: 100,
        target: '192.168.1.101',
        startTime: '2024-01-19 10:15:00',
        endTime: '2024-01-19 11:30:00',
        description: 'B区服务器安全扫描'
      }
    ]
  } catch (error) {
    ElMessage.error('获取任务列表失败')
  } finally {
    loading.value = false
  }
}

const handleViewDetails = (task: Task) => {
  selectedTask.value = task
  detailsDialogVisible.value = true
}

const getStatusType = (status: string) => {
  const types = {
    pending: 'info',
    running: 'warning',
    completed: 'success',
    failed: 'danger'
  }
  return types[status] || 'info'
}

const getStatusText = (status: string) => {
  const texts = {
    pending: '等待中',
    running: '执行中',
    completed: '已完成',
    failed: '失败'
  }
  return texts[status] || '未知'
}

onMounted(() => {
  fetchTasks()
})
</script>

<template>
  <div class="tasks-container">
    <div class="header">
      <h2>任务管理</h2>
    </div>

    <el-table v-loading="loading" :data="tasks" style="width: 100%">
      <el-table-column prop="name" label="任务名称" />
      <el-table-column prop="type" label="任务类型" />
      <el-table-column prop="status" label="状态">
        <template #default="{ row }">
          <el-tag :type="getStatusType(row.status)">
            {{ getStatusText(row.status) }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="progress" label="进度">
        <template #default="{ row }">
          <el-progress
            :percentage="row.progress"
            :status="row.status === 'failed' ? 'exception' : row.status === 'completed' ? 'success' : ''"
          />
        </template>
      </el-table-column>
      <el-table-column prop="target" label="目标" />
      <el-table-column prop="startTime" label="开始时间" />
      <el-table-column label="操作" width="120">
        <template #default="{ row }">
          <el-button type="primary" link @click="handleViewDetails(row)">查看详情</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 任务详情对话框 -->
    <el-dialog
      title="任务详情"
      v-model="detailsDialogVisible"
      width="600px"
    >
      <template v-if="selectedTask">
        <el-descriptions :column="1" border>
          <el-descriptions-item label="任务名称">{{ selectedTask.name }}</el-descriptions-item>
          <el-descriptions-item label="任务类型">{{ selectedTask.type }}</el-descriptions-item>
          <el-descriptions-item label="状态">
            <el-tag :type="getStatusType(selectedTask.status)">
              {{ getStatusText(selectedTask.status) }}
            </el-tag>
          </el-descriptions-item>
          <el-descriptions-item label="进度">
            <el-progress
              :percentage="selectedTask.progress"
              :status="selectedTask.status === 'failed' ? 'exception' : selectedTask.status === 'completed' ? 'success' : ''"
            />
          </el-descriptions-item>
          <el-descriptions-item label="目标">{{ selectedTask.target }}</el-descriptions-item>
          <el-descriptions-item label="开始时间">{{ selectedTask.startTime }}</el-descriptions-item>
          <el-descriptions-item label="结束时间">{{ selectedTask.endTime || '-' }}</el-descriptions-item>
          <el-descriptions-item label="任务描述">{{ selectedTask.description }}</el-descriptions-item>
        </el-descriptions>
      </template>
    </el-dialog>
  </div>
</template>

<style lang="scss" scoped>
.tasks-container {
  padding: 20px;

  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;

    h2 {
      margin: 0;
    }
  }
}
</style>