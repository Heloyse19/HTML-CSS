from .imports import request, session, redirect, render_template, url_for, BC, app, jsonify

def MainLogin():
    return render_template('MainLogin.html')


def login():
    #Desenvolver isso depois
    session['email'] = request.form['email']
    senha = request.form['senha']
    cadastros = BC.main()
    
    if cadastros:
        login_autorizado = False
        for dados in cadastros:
            print(dados['email'], dados['senha'])
            if dados['email'] == session['email'] and dados['senha'] == senha:
                login_autorizado = True
                break

        if login_autorizado:
            return jsonify({'sucess': True})
        
        #FAZER ESSA MENSAGEM APARECER E DESAPARECER CASO DE REFRESSH
        else:
            return jsonify({'Sucess': False, 'message' : 'Senha ou login incorretos'})
    
    else:
        return jsonify({'Sucess': False, 'message': 'Nenhum cadastro encontrado'})



