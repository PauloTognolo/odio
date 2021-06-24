import mysql.connector as mariadb
from flask import Flask

def teste ():
    mariadb_connection = mariadb.connect(user = 'root', password = 'admin', database = 'Test', host = 'localhost', port = 3306)
    cur = mariadb_connection.cursor()
    query_insert ="INSERT INTO usuarios (name, email, cpf, password) values ('jose', 'j@hotmail.com', '99999999989', '1234')"
    query_select = "SELECT * from usuarios"
    cur.execute(query_select)
    rows = cur.fetchall()
    print(rows)

    return 0
teste()