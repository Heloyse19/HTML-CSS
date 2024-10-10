from flask import Flask, url_for, session, request, redirect, render_template, jsonify
from routes import Tela_cadastro, Tela_login, Tela_recSenha, Tela_teste
app = Flask(__name__, template_folder='templates')
app.secret_key = '123'

@app.route('/')
def tela_login():
    return Tela_login.MainLogin()

@app.route('/login', methods=['POST'])
def Login():
    return Tela_login.login()


@app.route('/Cadastro.html', methods=['GET', 'POST'])
def tela_cadastro():
   return Tela_cadastro.tela_cadastro()

@app.route('/RecSenha.html')
def tela_recSenha():
    return Tela_recSenha.tela_recSenha()

@app.route('/teste')
def tela_teste():
    return Tela_teste.tela_teste()

if __name__ == '__main__':
    app.run(debug=True)