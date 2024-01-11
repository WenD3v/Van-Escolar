from flask import Blueprint, jsonify, make_response, request
from ..models import Van,db

vans_bp = Blueprint('vans',__name__)

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