import mysql.connector

def banco(hosti, username, senha, banco):
    return mysql.connector.connect(
        host = hosti,
        user = username,
        password = senha,
        database = banco
)

def registrar(cursor, login, email, senha,):
    inserir = 'INSERT INTO logins (login, email, senha) VALUES (%s, %s, %s)'
    cursor.execute(inserir,(login, email, senha))
def main(nome, eml, snh, metodo):
    conexao = banco(hosti='localhost', username='root', senha='teste', banco='login_site')
    cursor = conexao.cursor()
    if metodo == 'Cadastrar':
        registrar(cursor=cursor, login=nome, email=eml, senha=snh)
    
    conexao.commit()

