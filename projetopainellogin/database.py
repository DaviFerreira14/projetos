import sqlite3

conexao = sqlite3.connect('bancodedadoslogin.db')

cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    Senha TEXT NOT NULL,
    ConfSenha TEXT NOT NULL
)''')

print('Conexão ao banco de dados feita com sucesso!')