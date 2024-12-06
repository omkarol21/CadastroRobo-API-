from flask import Flask, render_template, g, request, redirect
import random
import sqlite3

def ligar_banco():
    banco = g._database = sqlite3.connect('API-Robo.db')
    return banco

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', Titulo='Home')

@app.route('/cadastrar')
def cadastrar():
    aleatorio = random.randint(1, 283175123912)
    url = f"https://robohash.org/{aleatorio}.png"
    imagemGerada = url
    return render_template('cadastro.html', Titulo='Cadastrar Robô', imagemrb=imagemGerada)

@app.route('/galeria')
def galeria():
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute('SELECT Descricao, Imagem FROM RobosAPI')
    imagens = cursor.fetchall()
    return render_template('galeria.html', Titulo='Galeria de Robôs', imagensrb=imagens)

@app.route('/criar', methods=['POST'])
def criar():
    imagem = request.form['url']
    descricao = request.form['descricao']

    banco = ligar_banco()
    cursor = banco.cursor()

    cursor.execute('INSERT INTO RobosAPI (Descricao, Imagem) VALUES (?,?);',(descricao, imagem))
    banco.commit()
    return redirect('/cadastrar')


if __name__ == '__main__':
    app.run()
