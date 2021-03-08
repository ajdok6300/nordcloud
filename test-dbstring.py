import os
basedir = os.path.abspath(os.path.dirname(__file__))
import urllib
import pyodbc

sql_database = os.environ['SQL_DATABASE']
sql_server = os.environ['SQL_SERVER']
sql_user = os.environ['SQL_USER']
sql_pwd = os.environ['SQL_PASSWORD']
SQLALCHEMY_DATABASE_URI = "mssql+pymssql://%s:%s@%s/%s" % (sql_user, sql_pwd, sql_server, sql_database )

print(sql_database)
print(sql_server)
print(sql_user)
print(sql_pwd)
print(SQLALCHEMY_DATABASE_URI)
print("DRIVER={ODBC Driver 17 for SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s;" % (sql_server, sql_database, sql_user, sql_pwd,))
