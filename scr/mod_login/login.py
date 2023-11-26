from flask import Blueprint, render_template, request, redirect, url_for
from funcoes import Funcoes

bp_login = Blueprint('login', __name__, url_prefix='/', template_folder='templates')

@bp_login.route("/", methods=['GET', 'POST'])
def login():
    return render_template("formLogin.html")

@bp_login.route('/login', methods=['POST'])
def validaLogin():
    try:
        cpf = request.form['usuario']
        senha = Funcoes.cifraSenha(request.form['senha'])
        if (cpf == "abc" and senha == Funcoes.cifraSenha('Bolinhas')):
            return redirect(url_for('index.formIndex'))
        else:
            raise Exception("Falha de Login! Verifique seus dados e tente novamente!")

    except Exception as e:
        return redirect(url_for('login.login', msgErro=e.args[0]))