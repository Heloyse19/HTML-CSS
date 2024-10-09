import mysql.connector
from urls import app, session, request
app.secret_key = '123'
def banco(hosti, username, senha, banco):
    return mysql.connector.connect(
        host = hosti,
        user = username,
        password = senha,
        database = banco
)



def registrar(cursor, nm, email, senha):
    inserir = 'INSERT INTO logins (login, email, senha) VALUES (%s, %s, %s)'
    cursor.execute(inserir,(nm, email, senha))

def login(cursor, email):
    cadastros = []
    cursor.execute(F'SELECT * FROM logins WHERE email = "{email}"')
    info = cursor.fetchall()
    for login in info:
        dict_cadastros = {}
        dict_cadastros['email'] = login[2]
        dict_cadastros['senha'] = login[3]
        cadastros.append(dict_cadastros)
    return cadastros


def main():
    conexao = banco(hosti='localhost', username='root', senha='teste', banco='login_site')
    cursor = conexao.cursor()
    if 'Cadastro.html' in request.referrer:
        registrar(cursor=cursor, nm=session['login'], email=session['email'], senha=session['senha'])
    
    elif '/' in request.referrer:
        return login(cursor=cursor, email=session['email'])
    else:
        print('Não esta indo para o Login')
    conexao.commit()

    conexao.close()
    cursor.close()

if __name__ == '__main__':
    main()

