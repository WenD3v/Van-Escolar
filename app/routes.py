from flask import Blueprint, jsonify, make_response, request
from .models import Cliente,Motorista,Van,Categoria,FormasPagamento,ContasReceber,ContasPagar,db

clientes_bp = Blueprint('clientes',__name__)
motoristas_bp = Blueprint('motoristas',__name__)
vans_bp = Blueprint('vans',__name__)
categorias_bp = Blueprint('categorias',__name__)
pagamentos_bp = Blueprint('formapagamentos',__name__)
contasreceber_bp = Blueprint('contasreceber',__name__)
contaspagar_bp = Blueprint('contaspagar',__name__)

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

@motoristas_bp.route('/motoristas/',methods=['GET'])
def get_motoristas():
    motoristas = Motorista.query.all()
    serialized_motoristas = [motorista.serialize() for motorista in motoristas]
    return make_response(
        jsonify(serialized_motoristas)
    )

@motoristas_bp.route('/motoristas/<id_motorista>',methods=['GET'])
def get_motorista_id(id_motorista):
    motorista = Motorista.query.get(id_motorista)
    if motorista:
        serialized_motorista = motorista.serialize()
        return make_response(
            jsonify(serialized_motorista)
        )
    else:
        return jsonify({'message': 'Motorista não encontrado'}), 404

@vans_bp.route('/vans/',methods=['GET'])
def get_vans():
    vans = Van.query.all()
    serialized_vans = [van.serialize() for van in vans]
    return make_response(
        jsonify(serialized_vans)
    )

@vans_bp.route('/vans/<int:id_van>',methods=['GET'])
def get_van_id(id_van):
    van = Van.query.get(id_van)
    if van:
        serialized_van = van.serialize()
        return make_response(jsonify(serialized_van))
    else:
        return jsonify({'message':'Van não encontrado'}), 404

@categorias_bp.route('/categorias/',methods=['GET'])
def get_categorias():
    categorias = Categoria.query.all()
    serialized_categorias = [categoria.serialize() for categoria in categorias]
    return make_response(
        jsonify(serialized_categorias)
    )

@categorias_bp.route('/categorias/<int:id_categoria>',methods=['GET'])
def get_categoria_id(id_categoria):
    categoria = Categoria.query.get(id_categoria)
    if categoria:
        serialized_categ = categoria.serialize()
        return make_response(jsonify(serialized_categ))
    
    else:
        return jsonify({'message':'Categoria não encontrado'}), 404

@pagamentos_bp.route('/formapagamentos/',methods=['GET'])
def get_pagamentos():
    pagamentos = FormasPagamento.query.order_by(FormasPagamento.id_pagamento.asc()).all()
    serialized_pagamentos = [pagamento.serialize() for pagamento in pagamentos]
    return make_response(
        jsonify(serialized_pagamentos)
    )

@pagamentos_bp.route('/formapagamentos/<int:id_pagamento>',methods=['GET'])
def get_pagamento_id(id_pagamento):
    pagamento = FormasPagamento.query.get(id_pagamento)
    if pagamento:
        serialized_pagamento = pagamento.serialize()
        return make_response(jsonify(serialized_pagamento))
    else:
        return jsonify({'message':'Forma de pagamento não encontrado'}), 404

@contasreceber_bp.route('/contas_receber/',methods=['GET'])
def get_titulos():
    titulos = ContasReceber.query.order_by(ContasReceber.data_vencimento.asc()).all()
    serialized_titulos = [titulo.serialize() for titulo in titulos]
    return make_response(
        jsonify(serialized_titulos)
    )

@contasreceber_bp.route('/contas_receber/<int:id_contas_receber>',methods=['GET'])
def get_titulo_id(id_contas_receber):
    titulo = ContasReceber.query.get(id_contas_receber)
    if titulo:
        serialized_titulo = titulo.serialize()
        return make_response(jsonify(serialized_titulo))
    else:
        return jsonify({'message':'Titulo não encontrado'}),404

@contaspagar_bp.route('/contas_pagar/',methods=['GET'])
def get_titulos():
    titulos = ContasPagar.query.order_by(ContasPagar.data_vencimento.asc()).all()
    serialized_titulos = [titulo.serialize() for titulo in titulos]
    return make_response(
        jsonify(serialized_titulos)
    )

@contaspagar_bp.route('/contas_pagar/<int:id_contas_pagar>',methods=['GET'])
def get_titulo_id(id_contas_pagar):
    titulo = ContasPagar.query.get(id_contas_pagar)
    if titulo:
        serialized_titulo = titulo.serialize()
        return make_response(jsonify(serialized_titulo))
    else:
        return jsonify({'message':'Titulo não encontrado'}),404