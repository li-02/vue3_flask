from flask import Blueprint, request
from flask_cors import CORS
from models.BookModel import BookModel
from extensions import db

bp = Blueprint('book', __name__, url_prefix='/api/book')
CORS(bp, resources={r"/api/*": {"origins": "*"}})


@bp.route('/getAllBooks/', methods=['GET'])
def get_all_books():
    books = BookModel.query.all()
    book_list = []
    for book in books:
        book_list.append(book.to_dict())
    return {'code': 0, 'msg': 'success', 'data': book_list}


@bp.route('/addBook/', methods=['POST'])
def add_book():
    book = request.json
    title = book['title']
    author = book['author']
    read = book['read']
    book_item = BookModel(title=title, author=author, read=read)
    db.session.add(book_item)
    db.session.commit()
    return {'code': 0, 'msg': 'success', 'data': {}}


@bp.route('/deleteBook/', methods=['POST'])
def delete_book():
    data = request.json
    id = data['id']
    book_item = BookModel.query.filter_by(id=id).first()
    db.session.delete(book_item)
    db.session.commit()
    return {'code': 0, 'msg': 'success', 'data': {'id': id}}


@bp.route('/updateBook/', methods=['POST'])
def update_book():
    data = request.json
    id = data['id']
    title = data['title']
    author = data['author']
    read = data['read']
    book_item = BookModel.query.filter_by(id=id).first()
    book_item.title = title
    book_item.author = author
    book_item.read = read
    db.session.commit()
    return {'code': 0, 'msg': 'success', 'data': {'id': id, 'title': title, 'author': author, 'read': read}}
