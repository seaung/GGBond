import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import { pinia } from './store'
import './style.css'

const app = createApp(App)

app.use(router)
app.use(ElementPlus)
app.use(pinia)

app.mount('#app')
