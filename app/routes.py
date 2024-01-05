from flask import Blueprint, jsonify, make_response
from .models import Cliente,Motorista,Van,Categoria,FormasPagamento

clientes_bp = Blueprint('clientes',__name__)
motoristas_bp = Blueprint('motoristas',__name__)
vans_bp = Blueprint('vans',__name__)
categorias_bp = Blueprint('categorias',__name__)
pagamentos_bp = Blueprint('formapagamentos',__name__)

@clientes_bp.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    serialized_clientes = [cliente.serialize() for cliente in clientes]
    return make_response(
        jsonify(serialized_clientes)
    )

@motoristas_bp.route('/motoristas',methods=['GET'])
def get_motoristas():
    motoristas = Motorista.query.all()
    serialized_motoristas = [motorista.serialize() for motorista in motoristas]
    return make_response(
        jsonify(serialized_motoristas)
    )

@vans_bp.route('/vans',methods=['GET'])
def get_vans():
    vans = Van.query.all()
    serialized_vans = [van.serialize() for van in vans]
    return make_response(
        jsonify(serialized_vans)
    )

@categorias_bp.route('/categorias',methods=['GET'])
def get_categorias():
    categorias = Categoria.query.all()
    serialized_categorias = [categoria.serialize() for categoria in categorias]
    return make_response(
        jsonify(serialized_categorias)
    )

@pagamentos_bp.route('/formapagamentos',methods=['GET'])
def get_pagamentos():
    pagamentos = FormasPagamento.query.order_by(FormasPagamento.id_pagamento.asc()).all()
    serialized_pagamentos = [pagamento.serialize() for pagamento in pagamentos]
    return make_response(
        jsonify(serialized_pagamentos)
    )

