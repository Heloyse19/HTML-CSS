
def MainLogin():
    from .imports import request, session, app, render_template, BC, url_for, redirect
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
                mensagem = 'Senha ou login incorretos'
        
        else:
            print('Login não encontrado')


        session.clear()
        return redirect(url_for('tela_login',mensagem=mensagem))

    return render_template('MainLogin.html')