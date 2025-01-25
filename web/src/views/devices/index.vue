<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'

interface Device {
  id: number
  name: string
  ip: string
  type: string
  status: 'online' | 'offline'
  lastSeen: string
}

const devices = ref<Device[]>([])
const loading = ref(true)
const dialogVisible = ref(false)
const isEdit = ref(false)

const deviceForm = ref<Device>({
  id: 0,
  name: '',
  ip: '',
  type: '',
  status: 'offline',
  lastSeen: ''
})

const fetchDevices = async () => {
  try {
    // TODO: 替换为实际的API调用
    await new Promise(resolve => setTimeout(resolve, 1000))
    devices.value = [
      {
        id: 1,
        name: '测试服务器-01',
        ip: '192.168.1.100',
        type: '服务器',
        status: 'online',
        lastSeen: '2024-01-20 15:30:00'
      },
      {
        id: 2,
        name: '测试服务器-02',
        ip: '192.168.1.101',
        type: '服务器',
        status: 'offline',
        lastSeen: '2024-01-19 10:15:00'
      }
    ]
  } catch (error) {
    ElMessage.error('获取设备列表失败')
  } finally {
    loading.value = false
  }
}

const handleAdd = () => {
  isEdit.value = false
  deviceForm.value = {
    id: 0,
    name: '',
    ip: '',
    type: '',
    status: 'offline',
    lastSeen: ''
  }
  dialogVisible.value = true
}

const handleEdit = (device: Device) => {
  isEdit.value = true
  deviceForm.value = { ...device }
  dialogVisible.value = true
}

const handleDelete = async (id: number) => {
  try {
    await ElMessageBox.confirm('确认删除该设备吗？', '提示', {
      type: 'warning'
    })
    // TODO: 实现删除逻辑
    ElMessage.success('删除成功')
    await fetchDevices()
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败')
    }
  }
}

const handleSubmit = async () => {
  try {
    // TODO: 实现提交逻辑
    await new Promise(resolve => setTimeout(resolve, 500))
    ElMessage.success(isEdit.value ? '更新成功' : '添加成功')
    dialogVisible.value = false
    await fetchDevices()
  } catch (error) {
    ElMessage.error(isEdit.value ? '更新失败' : '添加失败')
  }
}

onMounted(() => {
  fetchDevices()
})
</script>

<template>
  <div class="devices-container">
    <div class="header">
      <h2>设备管理</h2>
      <el-button type="primary" @click="handleAdd">添加设备</el-button>
    </div>

    <el-table v-loading="loading" :data="devices" style="width: 100%">
      <el-table-column prop="name" label="设备名称" />
      <el-table-column prop="ip" label="IP地址" />
      <el-table-column prop="type" label="设备类型" />
      <el-table-column prop="status" label="状态">
        <template #default="{ row }">
          <el-tag :type="row.status === 'online' ? 'success' : 'danger'">
            {{ row.status === 'online' ? '在线' : '离线' }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="lastSeen" label="最后在线时间" />
      <el-table-column label="操作" width="200">
        <template #default="{ row }">
          <el-button type="primary" link @click="handleEdit(row)">编辑</el-button>
          <el-button type="danger" link @click="handleDelete(row.id)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog
      :title="isEdit ? '编辑设备' : '添加设备'"
      v-model="dialogVisible"
      width="500px"
    >
      <el-form :model="deviceForm" label-width="100px">
        <el-form-item label="设备名称">
          <el-input v-model="deviceForm.name" />
        </el-form-item>
        <el-form-item label="IP地址">
          <el-input v-model="deviceForm.ip" />
        </el-form-item>
        <el-form-item label="设备类型">
          <el-input v-model="deviceForm.type" />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="handleSubmit">确定</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<style lang="scss" scoped>
.devices-container {
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