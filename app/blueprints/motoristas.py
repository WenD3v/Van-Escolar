from flask import Blueprint, jsonify, make_response, request
from ..models import Motorista,db

motoristas_bp = Blueprint('motoristas',__name__)

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