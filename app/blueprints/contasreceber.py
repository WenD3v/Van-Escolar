from flask import Blueprint, jsonify, make_response, request
from ..models import ContasReceber,db

contasreceber_bp = Blueprint('contasreceber',__name__)

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