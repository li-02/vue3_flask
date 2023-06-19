import api from '@/utils/api.js'

export function getBookList() {
    return api.get('/book/getAllBooks')
}
export function postAddBook(data) {
    return api.post('/book/addBook', data)
}
export function postUpdateBook(data) {
    return api.post('/book/updateBook', data)
}
export function postDeleteBook(data) {
    return api.post('/book/deleteBook', data)
}
