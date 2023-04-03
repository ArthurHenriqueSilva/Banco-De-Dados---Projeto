from flask import Flask, jsonify, request
from datetime import datetime


app = Flask(__name__)

class Usuario:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

usuarios = []

@app.route('/usuario/<int:cpf>', methods=['GET'])
def buscar_user():
    for usuario in usuarios:
        if usuario.cpf == cpf:
            usuario_json = {
                'cpf': usuario.cpf,
                'nome': usuario.nome,
                'data_nascimento': usuario.data_nascimento.isoformat()

            }
            return jsonify(usuario_json)
    return jsonify({'mensagem': 'Usuário não encontrado!!'}), 404

@app.route('/usuario', methods=['POST'])
def criar_user():
    cpf = int(request.json['cpf'])
    nome = request.json['nome']
    data_nascimento = datetime.strptime(request.json['data_nascimento'], '%Y-%m-%d' ).date()
    usuario = Usuario(cpf, nome, data_nascimento)
    usuarios.append(usuario)
    return jsonify({'mensagem':'Usuário criado!!'})


if __name__ == '__main__':
    app.run()