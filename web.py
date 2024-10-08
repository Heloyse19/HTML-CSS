from flask import Flask, url_for, session, request, redirect, render_template
import urls as url
app = Flask(__name__, template_folder='templates')
app.secret_key = '123'

@app.route('/', methods=['GET', 'POST'])
def tela_login():
    return url.MainLogin()

@app.route('/Cadastro.html', methods=['GET', 'POST'])
def tela_cadastro():
   return url.Tela_cadastro()

if __name__ == '__main__':
    app.run(debug=True)