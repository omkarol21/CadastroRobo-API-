import sqlite3

conexao = sqlite3.connect('API-Robo.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS RobosAPI(ID INTEGER PRIMARY KEY, Descricao TEXT, Imagem TEXT)')