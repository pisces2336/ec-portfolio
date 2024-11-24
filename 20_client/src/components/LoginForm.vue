<script setup lang="ts">
import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useCookies } from 'vue3-cookies'

const router = useRouter()
const { cookies } = useCookies()
const email = ref('')
const password = ref('')

const login = async () => {
  try {
    const res = await axios.post('api/auth/jwt/create', {
      email: email.value,
      password: password.value,
    })
    cookies.set('accessToken', res.data.access)

    alert('ログインに成功しました')
    router.push('/')
  } catch {
    alert('ログインに失敗しました')
  }
}
</script>

<template>
  <v-card title="ログイン">
    <v-card-text>
      <v-row>
        <v-col>
          <v-text-field label="メールアドレス" v-model="email"></v-text-field>
          <v-text-field label="パスワード" type="password" v-model="password"></v-text-field>
          <v-btn @click="login">送信</v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-btn variant="text">アカウントをお持ちでない方はこちら</v-btn>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>
