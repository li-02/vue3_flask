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
# it will be wrong if you set this in config.py, I don't know why
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:mysqlmima0210@127.0.0.1:3306/flask?charset=utf8'
# init db
db.init_app(app)
migrate = Migrate(app, db)
# register blueprint
app.register_blueprint(user_bp)
app.register_blueprint(book_bp)
CORS(app, **app.config['CORS_OPTIONS'])

if __name__ == '__main__':
    app.run()
