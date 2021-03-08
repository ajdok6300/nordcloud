import os
basedir = os.path.abspath(os.path.dirname(__file__))
import urllib
import pyodbc
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class Config(object):
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'notejam-flask-secret-key'
    WTF_CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'notejam-flask-secret-key'
    sql_database = os.environ['SQL_DATABASE']
    sql_server = os.environ['SQL_SERVER']
    sql_user = os.environ['SQL_USER']
    sql_pwd = os.environ['SQL_PASSWORD']
    params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s;" % (sql_server, sql_database, sql_user, sql_pwd,))
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params

class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False