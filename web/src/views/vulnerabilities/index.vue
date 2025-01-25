<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'

interface Vulnerability {
  id: number
  name: string
  severity: 'high' | 'medium' | 'low'
  status: 'open' | 'fixed'
  target: string
  discoveredAt: string
  description: string
}

const vulnerabilities = ref<Vulnerability[]>([])
const loading = ref(true)
const scanDialogVisible = ref(false)
const detailsDialogVisible = ref(false)
const selectedVulnerability = ref<Vulnerability | null>(null)

const scanForm = ref({
  target: '',
  scanType: 'full'
})

const fetchVulnerabilities = async () => {
  try {
    // TODO: 替换为实际的API调用
    await new Promise(resolve => setTimeout(resolve, 1000))
    vulnerabilities.value = [
      {
        id: 1,
        name: 'SQL注入漏洞',
        severity: 'high',
        status: 'open',
        target: '192.168.1.100',
        discoveredAt: '2024-01-20 15:30:00',
        description: '在登录接口发现SQL注入漏洞，可能导致未授权访问数据库。'
      },
      {
        id: 2,
        name: 'XSS漏洞',
        severity: 'medium',
        status: 'fixed',
        target: '192.168.1.101',
        discoveredAt: '2024-01-19 10:15:00',
        description: '在用户输入处发现跨站脚本漏洞，可能导致恶意脚本执行。'
      }
    ]
  } catch (error) {
    ElMessage.error('获取漏洞列表失败')
  } finally {
    loading.value = false
  }
}

const handleStartScan = () => {
  scanDialogVisible.value = true
}

const handleScanSubmit = async () => {
  try {
    // TODO: 实现扫描任务提交逻辑
    await new Promise(resolve => setTimeout(resolve, 500))
    ElMessage.success('扫描任务已提交')
    scanDialogVisible.value = false
    await fetchVulnerabilities()
  } catch (error) {
    ElMessage.error('提交扫描任务失败')
  }
}

const handleViewDetails = (vuln: Vulnerability) => {
  selectedVulnerability.value = vuln
  detailsDialogVisible.value = true
}

const getSeverityType = (severity: string) => {
  const types = {
    high: 'danger',
    medium: 'warning',
    low: 'info'
  }
  return types[severity] || 'info'
}

const getStatusType = (status: string) => {
  return status === 'fixed' ? 'success' : 'danger'
}

onMounted(() => {
  fetchVulnerabilities()
})
</script>

<template>
  <div class="vulnerabilities-container">
    <div class="header">
      <h2>漏洞扫描</h2>
      <el-button type="primary" @click="handleStartScan">开始扫描</el-button>
    </div>

    <el-table v-loading="loading" :data="vulnerabilities" style="width: 100%">
      <el-table-column prop="name" label="漏洞名称" />
      <el-table-column prop="severity" label="严重程度">
        <template #default="{ row }">
          <el-tag :type="getSeverityType(row.severity)">
            {{ row.severity === 'high' ? '高' : row.severity === 'medium' ? '中' : '低' }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="status" label="状态">
        <template #default="{ row }">
          <el-tag :type="getStatusType(row.status)">
            {{ row.status === 'fixed' ? '已修复' : '未修复' }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="target" label="目标" />
      <el-table-column prop="discoveredAt" label="发现时间" />
      <el-table-column label="操作" width="120">
        <template #default="{ row }">
          <el-button type="primary" link @click="handleViewDetails(row)">查看详情</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 扫描配置对话框 -->
    <el-dialog
      title="新建扫描任务"
      v-model="scanDialogVisible"
      width="500px"
    >
      <el-form :model="scanForm" label-width="100px">
        <el-form-item label="扫描目标">
          <el-input v-model="scanForm.target" placeholder="请输入IP地址或域名" />
        </el-form-item>
        <el-form-item label="扫描类型">
          <el-select v-model="scanForm.scanType" style="width: 100%">
            <el-option label="完整扫描" value="full" />
            <el-option label="快速扫描" value="quick" />
            <el-option label="自定义扫描" value="custom" />
          </el-select>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="scanDialogVisible = false">取消</el-button>
        <el-button type="primary" @click="handleScanSubmit">开始扫描</el-button>
      </template>
    </el-dialog>

    <!-- 漏洞详情对话框 -->
    <el-dialog
      title="漏洞详情"
      v-model="detailsDialogVisible"
      width="600px"
    >
      <template v-if="selectedVulnerability">
        <el-descriptions :column="1" border>
          <el-descriptions-item label="漏洞名称">{{ selectedVulnerability.name }}</el-descriptions-item>
          <el-descriptions-item label="严重程度">
            <el-tag :type="getSeverityType(selectedVulnerability.severity)">
              {{ selectedVulnerability.severity === 'high' ? '高' : selectedVulnerability.severity === 'medium' ? '中' : '低' }}
            </el-tag>
          </el-descriptions-item>
          <el-descriptions-item label="状态">
            <el-tag :type="getStatusType(selectedVulnerability.status)">
              {{ selectedVulnerability.status === 'fixed' ? '已修复' : '未修复' }}
            </el-tag>
          </el-descriptions-item>
          <el-descriptions-item label="目标">{{ selectedVulnerability.target }}</el-descriptions-item>
          <el-descriptions-item label="发现时间">{{ selectedVulnerability.discoveredAt }}</el-descriptions-item>
          <el-descriptions-item label="漏洞描述">{{ selectedVulnerability.description }}</el-descriptions-item>
        </el-descriptions>
      </template>
    </el-dialog>
  </div>
</template>

<style lang="scss" scoped>
.vulnerabilities-container {
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