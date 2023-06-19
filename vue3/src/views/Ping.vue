<template>
    <div class="container">
        <button type="button" class="btn btn-primary" @click="toPong">{{ msg }}</button>
    </div>
</template>

<script>
import router from '@/router/index.js';

export default {
    name: 'PingView',
    setup() {
        let msg = 'Ping'
        function toPong() {
            router.push({ path: '/pong' })
        }
        return {
            msg, toPong
        }
    }
}
</script>

<style scoped></style>