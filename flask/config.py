# config.py

# 允许跨域,如果要指定源地址，可以在origins中指定https://example.com
CORS_OPTIONS = {
    'supports_credentials': True,
    'resources': {
        r"/api/*": {"origins": "*"}
    }
}

# 配置数据库
DB_CONFIG = {
    'HOST': '127.0.0.1',
    'PORT': '3306',
    'USER': 'root',
    'PASSWORD': 'mysqlmima0210',
    'DATABASE': 'flask',
    'CHARSET': 'utf8',
}

DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    DB_CONFIG['USER'], DB_CONFIG['PASSWORD'], DB_CONFIG['HOST'],
    DB_CONFIG['PORT'], DB_CONFIG['DATABASE']
)

