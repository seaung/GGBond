import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUserStore = defineStore('user', () => {
  const token = ref('')
  const userInfo = ref({
    username: '',
    avatar: ''
  })

  const setToken = (newToken: string) => {
    token.value = newToken
    localStorage.setItem('token', newToken)
  }

  const setUserInfo = (info: { username: string; avatar: string }) => {
    userInfo.value = info
  }

  const logout = () => {
    token.value = ''
    userInfo.value = {
      username: '',
      avatar: ''
    }
    localStorage.removeItem('token')
  }

  return {
    token,
    userInfo,
    setToken,
    setUserInfo,
    logout
  }
})