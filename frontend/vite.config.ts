import { defineConfig } from 'vite'
import { resolve } from 'path';
import vue from '@vitejs/plugin-vue'

const pathResolve = (dir: string): string => {
    return resolve(__dirname, ".", dir);
};

const alias: Record<string, string> = {
    "@": pathResolve("src"),
    "@build": pathResolve("build")
};

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
      alias
  }
})
