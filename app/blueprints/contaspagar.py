from flask import Blueprint, jsonify, make_response, request
from ..models import ContasPagar,db

contaspagar_bp = Blueprint('contaspagar',__name__)

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