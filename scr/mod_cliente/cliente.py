from flask import Blueprint, render_template, request, redirect, url_for
import requests
from funcoes import Funcoes
from settings import HEADERS_API, ENDPOINT_CLIENTE

bp_cliente = Blueprint('cliente', __name__, url_prefix="/cliente", template_folder='templates')

''' rotas dos formulários '''
@bp_cliente.route('/insert', methods=['POST'])
def insert():
    try:
        # dados enviados via FORM
        id_cliente = request.form['id']
        nome = request.form['nome']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        compra_fiado = request.form['compra_fiado']
        dia_fiado = request.form['dia_fiado']
        senha = Funcoes.cifraSenha(request.form['senha'])

        # monta o JSON para envio a API
        payload = {'id_cliente': id_cliente, 'nome': nome, 'cpf': cpf, 'telefone': telefone, 'compra_fiado': compra_fiado, 'dia_fiado': dia_fiado, 'senha': senha}
        
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(ENDPOINT_CLIENTE, headers=HEADERS_API, json=payload)
        result = response.json()

        print(result) # [{'msg': 'Cadastrado com sucesso!', 'id': 13}, 200]
        print(response.status_code) # 200

        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])

        return render_template('formListaCliente.html', msg=result[0])

    except Exception as e:
        return render_template('formListaCliente.html',  msgErro=e.args[0])

@bp_cliente.route('/', methods=['GET', 'POST'])
def formListaCliente():
    try:
        response = requests.get(ENDPOINT_CLIENTE, headers=HEADERS_API)
        result = response.json()

        if (response.status_code != 200):
            raise Exception(result[0])
        return render_template('formListaCliente.html', result=result[0])
   
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])

@bp_cliente.route('/form-cliente/', methods=['GET' , 'POST'])
def formCliente():
    return render_template('formCliente.html')

@bp_cliente.route("/form-edit-cliente", methods=['POST'])
def formEditCliente():
    try:
        id_cliente = request.form['id']
        response = requests.get(ENDPOINT_CLIENTE + id_cliente, headers=HEADERS_API)
        result = response.json()

        if (response.status_code != 200):
            raise Exception(result[0])
        return render_template('formCliente.html', result=result[0])
   
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])
    
@bp_cliente.route('/edit', methods=['POST'])
def edit():
    try:
        id_cliente = request.form['id']
        nome = request.form['nome']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        compra_fiado = request.form['compra_fiado']
        dia_fiado = request.form['dia_fiado']
        senha = Funcoes.cifraSenha(request.form['senha'])

        payload = {'id_cliente': id_cliente, 'nome': nome, 'cpf': cpf, 'telefone': telefone, 'compra_fiado': compra_fiado, 'dia_fiado': dia_fiado, 'senha': senha}

        response = requests.put(ENDPOINT_CLIENTE + id_cliente, headers=HEADERS_API, json=payload)
        result = response.json()

        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])
        return redirect(url_for('cliente.formListaCliente', msg=result[0]))

    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])