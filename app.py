from datetime import date
from flask import Flask, request, jsonify

app = Flask(__name__)

class Usuario:
    def __init__(self, cpf: int, nome: str, data_nascimento: date):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

usuarios = []

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    print("Requisição recebida para /usuarios")
    return jsonify([{'cpf':usuario.cpf, 'nome':usuario.nome, 'data_nascimento':usuario.data_nascimento.isoformat()} for usuario in usuarios])

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    cpf = int(dados['cpf'])
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return jsonify({'erro': 'Já existe um usuário com o CPF informado'}), 409
    try:
        usuario = Usuario(cpf, dados['nome'], date.fromisoformat(dados['data_nascimento']))
    except ValueError:
        return jsonify({'erro': 'Data de nascimento inválida. Utilize o formato yyyy-mm-dd.'}), 400
    usuarios.append(usuario)
    return jsonify({'cpf':usuario.cpf, 'nome':usuario.nome, 'data_nascimento': usuario.data_nascimento.isoformat()})

@app.route('/usuarios/<int:cpf>', methods=['GET'])
def buscar_usuario(cpf):
    print("Requisição recebida para /usuarios/{}".format(cpf))
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return jsonify({'cpf':usuario.cpf, 'nome':usuario.nome, 'data_nascimento': usuario.data_nascimento.isoformat()})
    return jsonify({'erro': 'Usuário não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
