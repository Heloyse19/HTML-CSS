def tela_recSenha():
    from .imports import request, session, redirect, render_template, url_for, BC, app
    app.secret_key = '123'



    return render_template('RecSenha.html')