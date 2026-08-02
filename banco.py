import mysql.connector
import os

def conectar():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "******",
        port = 3306,
        database = "teste_python"
    )
    return conexao
