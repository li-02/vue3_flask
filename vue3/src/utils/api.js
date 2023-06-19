import axios from 'axios'
// 走的代理服务器的端口，所以请求的是代理服务器的端口
const baseURL = 'http://localhost:5173/api'  // 这里设置你的基础接口路径

const api = axios.create({
    baseURL: baseURL,
    timeout: 5000,  // 设置请求超时时间
})

// 请求拦截器
// api.interceptors.request.use(
//     config => {
//         // 在请求发送之前，在这里处理公共逻辑，如添加请求头等
//         return config
//     },
//     error => {
//         // 对请求错误做处理
//         return Promise.reject(error)
//     }
// )

// // 响应拦截器
// api.interceptors.response.use(
//     response => {
//         // 在这里处理响应数据，如处理通用的错误码等
//         return response.data
//     },
//     error => {
//         // 对响应错误做处理
//         return Promise.reject(error)
//     }
// )

export default api