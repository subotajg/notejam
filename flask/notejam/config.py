import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'notejam-flask-secret-key'
    WTF_CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'notejam-flask-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'notejam.db')


class ProductionConfig(Config):
    DEBUG = False
    user = os.getenv('RDS_USERNAME', '')
    password = os.getenv('RDS_PASSWORD', '')
    host = os.getenv('RDS_HOSTNAME', '')
    db_name = os.getenv('RDS_DB_NAME', '')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + user + ':' + password + '@' + host + '/' + db_name


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
