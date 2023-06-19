import api from '@/utils/api.js'

export function userLogin(data) {
    return api.post('/user/login', data)
}

export function userRegister(data) {
    return api.post('/user/register', data)
}