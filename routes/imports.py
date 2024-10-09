from web import Flask, url_for, session, request, redirect, render_template, app
from routes import Tela_cadastro, Tela_login, Tela_recSenha, Tela_teste
from bancos_dados import Banco_cadastro as BC