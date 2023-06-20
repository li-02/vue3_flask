<template>
    <div class="form">
        <div class="p-container">
            <p @click="toggleLoginRegister('login')" :class="{ active: showLogin }">log in</p>
            <p @click="toggleLoginRegister('register')" :class="{ active: showRegister }">set up</p>
        </div>

        <div v-if="showLogin">
            <el-form label-position="top">
                <el-form-item label="Username">
                    <el-input v-model="user.username" placeholder="Username"></el-input>
                </el-form-item>
                <el-form-item label="Password">
                    <el-input v-model="user.password" placeholder="Password"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-link :underline="false">forget password?</el-link>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="login">Login</el-button>
                </el-form-item>
            </el-form>
        </div>
        <div v-if="showRegister">
            <el-form label-position="top">
                <el-form-item label="Username">
                    <el-input v-model="registerUser.username" placeholder="Username"></el-input>
                </el-form-item>
                <el-form-item label="Password">
                    <el-input type="password" show-password v-model="registerUser.password"
                        placeholder="Password"></el-input>
                </el-form-item>
                <el-form-item label="check-Password">
                    <el-input type="password" show-password v-model="registerUser.checkPassword"
                        placeholder="check-Password"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="register">register</el-button>
                </el-form-item>
            </el-form>

        </div>
    </div>
</template>

<script>
import { reactive, ref } from 'vue'
import { userLogin, userRegister } from '@/utils/user.js'
import router from '@/router/index.js'
export default {
    name: 'LoginView',
    setup() {

        let user = reactive({
            username: '',
            password: ''
        })
        let showLogin = ref(true)
        let showRegister = ref(false)
        let registerUser = reactive({
            username: '',
            password: '',
            checkPassword: ''
        })
        function login() {
            console.log(user)
            userLogin({ 'username': user.username, 'password': user.password }).then(res => {
                console.log(res)
                router.replace({ path: '/books' })
            }).catch(err => {
                console.log(err)
            })
        }
        function register() {
            console.log(registerUser)
            userRegister(registerUser).then(res => {
                console.log(res)
            }).catch(err => {
                console.log(err)
            })
        }
        function toggleLoginRegister(value) {
            if (value === 'login') {
                showLogin.value = true
                showRegister.value = false
            } else {
                showLogin.value = false
                showRegister.value = true
            }
        }


        return {
            user, login, showLogin, showRegister, registerUser, toggleLoginRegister, register
        }
    }
}
</script>
<style scoped>
.form {
    position: absolute;
    /*设置定位方式为绝对定位*/
    top: 50%;
    /*将顶部边缘设置在其父元素的中心*/
    left: 50%;
    /*将左边边缘设置在其父元素的中心*/
    transform: translate(-50%, -50%);
    /*将元素向左向上移动其自身一半的宽度和高度，以便将其中心点与父元素的中心点对齐*/

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 500px;
    height: 500px;
    padding: 20px;
    border: 2px solid #070707;
    border-radius: 5px;
}

.p-container {
    display: flex;
}

.p-container p {
    cursor: pointer;
    padding: 10px;
    margin-right: 10px;
}

.p-container p.active {
    background-color: #ddd;
}

.p-container p:hover {
    background-color: #eee;
}
</style>

