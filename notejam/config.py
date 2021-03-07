import os
basedir = os.path.abspath(os.path.dirname(__file__))
import urllib
import pyodbc

class Config(object):
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'notejam-flask-secret-key'
    WTF_CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'notejam-flask-secret-key'
    DB_STRING = os.environ["DB_STRING"]
    #params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};SERVER=notejam-db.database.windows.net;DATABASE=notejam-db;UID=notejam-sql;PWD=H5WAqjcN5N5Bcazf!")
    #params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=notejam-db.database.windows.net;DATABASE=notejam-db;UID=notejam-sql;PWD=H5WAqjcN5N5Bcazf!")
    params = urllib.parse.quote_plus(DB_STRING)
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'notejam.db')


class ProductionConfig(Config):
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
