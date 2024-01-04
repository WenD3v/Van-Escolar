import mysql.connector
from flask import Flask, make_response, jsonify, request

mydb = mysql.connector.connect(host='localhost',user="root",password='admin',database='van')

app = Flask(__name__)
app.debug = True
app.config['JSON_SORT_KEY'] = False

@app.route('/clientes', methods=['GET'])
def get_carros():
    my_cursor = mydb.cursor()
    my_cursor.execute('select * from cliente')
    meus_clientes = my_cursor.fetchall()
    clientes = list()
    for cliente in meus_clientes:
        clientes.append(
            {
                'id_cliente': cliente[0],
                'ativo': cliente[1],
                'data_cadastro': cliente[2],
                'cpf': cliente[3],
                'nome': cliente[4],
                'celular': cliente[5],
                'telefone' : cliente[6]
            }
        )
    return make_response(
        jsonify(
            mensagem='lista de clientes',
            dados=clientes
        )
    )

app.run()