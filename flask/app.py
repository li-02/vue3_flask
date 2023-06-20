from flask import Flask
import config
from blueprints.user import bp as user_bp
from blueprints.book import bp as book_bp
from extensions import db
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
# setting config
app.config.from_object(config)
# set db uri
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
# 初始化db
db.init_app(app)
migrate = Migrate(app, db)
# 注册蓝图，每个都要注册
app.register_blueprint(user_bp)
app.register_blueprint(book_bp)
CORS(app, **app.config['CORS_OPTIONS'])

if __name__ == '__main__':
    app.run()
