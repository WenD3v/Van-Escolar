from flask import Blueprint, jsonify, make_response, request
from ..models import FormasPagamento,db

pagamentos_bp = Blueprint('formapagamentos',__name__)

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