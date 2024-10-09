def tela_cadastro():
    from .imports import request, session, redirect, render_template, url_for, BC, app
    app.secret_key = '123'



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
