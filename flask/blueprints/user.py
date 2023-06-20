from flask import Blueprint, request, jsonify, make_response
from models.UserModel import UserModel as User
from extensions import db
from flask_cors import CORS

bp = Blueprint('user', __name__, url_prefix='/api/user')

CORS(bp, resources={r"/api/*": {"origins": "*"}})


# /user/login
@bp.route('/login/', methods=['POST', 'OPTIONS'])
def login():
    response = make_response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    if request.method == 'OPTIONS':
        # 处理 OPTIONS 请求，返回跨域请求所需的响应头
        response=jsonify({'code': 0, 'msg': 'success'})
        return response
    else:
        user = request.json  # get the axios post data
        username = user['username']
        password = user['password']
        userInDB = User.query.filter_by(username=username).first()
        if userInDB:
            if password == userInDB.password:  # UserModel dont support [''] to get the value
                response = jsonify({'code': 0, 'msg': '登录成功', 'data': {username: username}})
                return response
            else:
                return jsonify({'code': 1, 'msg': '密码错误'})
        else:
            return jsonify({'code': 1, 'msg': '用户名不存在'})


# /user/register
@bp.route('/register/', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        # 处理 OPTIONS 请求，返回跨域请求所需的响应头
        return jsonify({'code': 0, 'msg': 'success'})
    else:
        registerUser = request.json['registerUser']
        username = registerUser['username']
        usernameInDB = User.query.filter_by(username=username).first()
        if usernameInDB:
            return jsonify({'code': 1, 'msg': '用户名已存在'})
        else:
            password = registerUser['password']
            user = User(username=username, password=password, email='')
            db.session.add(user)
            db.session.commit()
            response = jsonify({'code': 0, 'msg': '注册成功', 'data': {'username': username}})
            return response
