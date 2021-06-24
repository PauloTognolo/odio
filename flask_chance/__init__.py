from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import mysql.connector as mariadb

app = Flask(__name__)

##### Parte de conexão com o banco de dados que não deu tempo #####

#mariadb_connection = mariadb.connect(user = 'root', password = 'admin', database = 'test2', host = 'localhost', port = 3306)
#app.config['SQLALCHEMY_DATABASE_URI'] = mariadb_connection

#create_cursor = mariadb_connection.cursor()

##############

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flask_chance import routes
