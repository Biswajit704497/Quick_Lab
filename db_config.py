import os
from flask_mysqldb import MySQL


mysql = MySQL()

def init_mysql(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'quicklab'
    app.config['MYSQL_PORT'] =3306

    return MySQL(app)   