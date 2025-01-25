import { createPinia } from 'pinia'
import { useUserStore } from './user'

export const pinia = createPinia()

export {
  useUserStore
}