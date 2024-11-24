<script setup lang="ts">
import axios from 'axios'
import { RouterView, useRoute, useRouter } from 'vue-router'
import { useCookies } from 'vue3-cookies'

const { cookies } = useCookies()
const accessToken = cookies.get('accessToken')
const router = useRouter()
const route = useRoute()

// token検証
axios.post('api/jwt/verify', { token: accessToken }).catch(() => {
  if (route.path !== '/login') {
    alert('ログインが必要です。')
    router.push('login')
  }
})
</script>

<template>
  <main>
    <RouterView />
  </main>
</template>

<style scoped></style>
