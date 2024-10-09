from flask import Flask, url_for, session, request, redirect, render_template
from web import app
from bancos_dados import Banco_cadastro as BC
app.secret_key = '123'

def MainLogin():
    #Desenvolver isso depois
    if request.method == 'POST':
        session['email'] = request.form.get('email')
        session['senha'] = request.form.get('senha')
        cadastros = BC.main()
        
        if cadastros:
            login_autorizado = False
            for dados in cadastros:
                print(dados['email'], dados['senha'])
                if dados['email'] == session['email'] and dados['senha'] == session['senha']:
                    login_autorizado = True
                    break

            if login_autorizado:
               return redirect(url_for('tela_teste'))
            
            #FAZER ESSA MENSAGEM APARECER E DESAPARECER CASO DE REFRESSH
            else:
                session['mensagem'] = 'Senha ou login incorretos'
        
        else:
            print('Login não encontrado')


        session.clear()
        return redirect(url_for('tela_login', mensagem=session['mensagem']))

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

def tela_teste():
    return render_template('Tela_teste.html')