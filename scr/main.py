from flask import Flask, render_template

app = Flask(__name__)

from mod_funcionario.funcionario import bp_funcionario
app.register_blueprint(bp_funcionario)

from mod_index.index import bp_index
app.register_blueprint(bp_index)

from mod_cliente.cliente import bp_cliente
app.register_blueprint(bp_cliente)

from mod_produto.produto import bp_produto
app.register_blueprint(bp_produto)

from settings import HOST, PORT, DEBUG

''' chamadas dos formulários '''
@app.route('/')
def formIndex():
    return render_template('formListaIndex.html'), 200

@app.route('/funcionario/')
def formListaFuncionario():
    return render_template('formListaFuncionario.html'), 200

@app.route('/cliente/')
def formListaCliente():
    return render_template('formListaCliente.html'), 200

@app.route('/produto/')
def formListaProduto():
   return render_template('formListaProduto.html'), 200

if __name__ == "__main__":
    """ Inicia o aplicativo WEB Flask """
app.run(host=HOST, port=PORT, debug=DEBUG)