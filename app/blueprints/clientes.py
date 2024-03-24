from flask import Blueprint, jsonify, make_response, request
from ..models import Cliente,db

clientes_bp = Blueprint('clientes',__name__)

@clientes_bp.route('/clientes/', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    serialized_clientes = [cliente.serialize() for cliente in clientes]
    return make_response(
        jsonify(serialized_clientes)
    )

@clientes_bp.route('/clientes/<int:id_cliente>',methods=['GET'])
def get_cliente_id(id_cliente):
    cliente = Cliente.query.get(id_cliente)
    if cliente:
        serialized_cliente = cliente.serialize()
        return make_response(
            jsonify(serialized_cliente)
        )
    else:
        return jsonify({'message': 'Cliente não encontrado'}), 404
    
@clientes_bp.route('/clientes/',methods=['POST'])
def cadastra_cliente():
    dados = request.json
    novo_cliente = Cliente(
        cpf=dados.get('CPF'),
        nome=dados.get('NOME'),
        celular=dados.get('CELULAR'),
        telefone=dados.get('TELEFONE')
    )
    db.session.add(novo_cliente)
    db.session.commit()

    serialized_novo_cliente = novo_cliente.serialize()
    return make_response(jsonify(serialized_novo_cliente),201)

@clientes_bp.route('/clientes/<int:id_cliente>',methods=['PUT'])
def edita_cliente(id_cliente):
    cliente = Cliente.query.get(id_cliente)
    if cliente:
        novos_dados = request.json
        
        cliente.cpf=novos_dados.get('CPF')
        cliente.nome=novos_dados.get('NOME')
        cliente.celular=novos_dados.get('CELULAR')
        cliente.telefone=novos_dados.get('TELEFONE')
        
        db.session.commit()

        serialized_novo_cliente = cliente.serialize()
        return make_response(jsonify(serialized_novo_cliente),201)
    
    else:
        return jsonify({'message':'Cliente não encontrado'}), 404
    

@clientes_bp.route('/clientes/<int:id_cliente>',methods=['DELETE'])
def remove_cliente(id_cliente):
    cliente = Cliente.query.get(id_cliente)
    if cliente:
        db.session.delete(cliente)
        db.session.commit()

        serialized_novo_cliente = cliente.serialize()
        return make_response(jsonify(serialized_novo_cliente),201)
    
    else:
        return jsonify({'message':'Cliente não encontrado'}), 404