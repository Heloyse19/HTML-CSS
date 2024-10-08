from flask import Flask, url_for, session, request, redirect, render_template
from web import app
from bancos_dados import Banco_cadastro as BC
app.secret_key = '123'

def MainLogin():
    #Desenvolver isso depois
    if request.method == 'POST':
        cadastros = BC.main()
        print(cadastros)
        session.clear()
        return redirect(url_for('tela_login'))

    return render_template('MainLogin.html')


def Tela_cadastro():
    if request.method == 'POST':
        login = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('Senha')

        session['login'] = login
        session['email'] = email
        session['senha'] = senha
        BC.main()
        
        session.clear()
        return redirect(url_for('tela_cadastro'))
    
    return render_template('Cadastro.html')

def tela_recSenha():
    return render_template('RecSenha.html')