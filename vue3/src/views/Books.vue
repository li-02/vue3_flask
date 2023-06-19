<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-10">
                <h1>Books</h1>
                <hr><br><br>
                <button type="button" class="btn btn-success btn-sm" @click="showDialog(null)">Add Book</button>
                <br><br>
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">Title</th>
                            <th scope="col">Author</th>
                            <th scope="col">Read?</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="book in books" :key="book.id">
                            <td>{{ book.title }}</td>
                            <td>{{ book.author }}</td>
                            <td>
                                <span v-if="book.read">Yes</span>
                                <span v-else>No</span>
                            </td>
                            <td>
                                <div class="btn-group" role="group">
                                    <button type="button" class="btn btn-warning btn-sm"
                                        @click="showDialog(book.id)">Update</button>
                                    <button type="button" class="btn btn-danger btn-sm"
                                        @click="deleteBook(book.id)">Delete</button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    <!-- dialog -->
    <div>
        <el-dialog v-model="addFormVisible">
            <div>
                <div class="modal-header">
                    <h5 class="modal-title">{{ type === 'add' ? 'Add Book' : 'Update Book' }}</h5>
                </div>
                <div class="modal-body">
                    <form>
                        <div class="mb-3">
                            <label for="addBookTitle" class="form-label">Title:</label>
                            <input type="text" class="form-control" id="addBookTitle" v-model="addBookForm.title"
                                placeholder="Enter title">
                        </div>
                        <div class="mb-3">
                            <label for="addBookAuthor" class="form-label">Author:</label>
                            <input type="text" class="form-control" id="addBookAuthor" v-model="addBookForm.author"
                                placeholder="Enter author">
                        </div>
                        <div class="mb-3 form-check">
                            <input type="checkbox" class="form-check-input" id="addBookRead" v-model="addBookForm.read">
                            <label class="form-check-label" for="addBookRead">Read?</label>
                        </div>
                        <div class="btn-group" role="group">
                            <button type="button" class="btn btn-primary btn-sm" @click="handleAddSubmit(type, id)">
                                Submit
                            </button>
                            <button type="button" class="btn btn-danger btn-sm" @click="handleAddReset">
                                Reset
                            </button>
                        </div>
                    </form>

                </div>
            </div>
        </el-dialog>
    </div>
</template>

<script>
import { onBeforeMount, reactive, ref } from 'vue';
import { postAddBook, postDeleteBook, postUpdateBook } from '@/utils/book.js'
import { getBookList } from "@/utils/book.js";
export default {
    name: 'BooksView',
    setup() {
        let books = reactive([])
        let addBookForm = reactive({
            title: '',
            author: '',
            read: [],
        })
        let type = ref('add')
        let bookId = ref(null)
        let addFormVisible = ref(false)

        function initForm() {
            addBookForm.title = '';
            addBookForm.author = '';
            addBookForm.read = false;
        }
        onBeforeMount(() => {
            getAllBooks()
        })
        function getAllBooks() {
            getBookList().then(res => {
                // books = res.data.data vue3无法监测到对象的改变，只能检测到对象的属性的改变
                books.splice(0, books.length, ...res.data.data)
            }).catch(err => {
                console.log(err)
            })
        }
        function addBook(data) {
            postAddBook(data).then(() => {
                getAllBooks()
            }).catch((err) => {
                console.log(err)
            })
        }
        function deleteBook(id) {
            postDeleteBook({ id }).then(() => {
                getAllBooks()
            }).catch((err) => {
                console.log(err)
            })
        }
        function handleAddSubmit() {
            let payload = {
                title: addBookForm.title,
                author: addBookForm.author,
                read: Boolean(addBookForm.read), // property shorthand
            }
            if (type.value === 'update') {
                payload.id = bookId.value
                postUpdateBook(payload)
                getAllBooks()
            } else {
                addBook(payload)
            }
            addFormVisible.value = false;
            initForm();
        }
        function handleAddReset() {
            initForm()
        }
        function showDialog(id = null) {
            if (id !== null) {
                type.value = 'update'
                bookId.value = id
                for (let i = 0; i < books.length; i++) {
                    if (books[i].id === id) {
                        addBookForm.title = books[i].title
                        addBookForm.author = books[i].author
                        addBookForm.read = books[i].read
                        break
                    }
                }
            } else {
                type.value = 'add'
            }
            addFormVisible.value = true
        }

        return {
            books, addBookForm, type, bookId, addFormVisible, handleAddSubmit, handleAddReset, deleteBook, showDialog
        }
    }
}

</script>