import os

from flask_mysqldb import MySQL


mysql = MySQL()

def init_mysql(app):
    app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
    app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
    app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
    app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")
    app.config['MYSQL_PORT'] =56210

    return MySQL(app)   