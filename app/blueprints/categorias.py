from flask import Blueprint, jsonify, make_response, request
from ..models import Categoria,db

categorias_bp = Blueprint('categorias',__name__)

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