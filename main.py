import mysql.connector
from flask import Flask, make_response, jsonify, request

mydb = mysql.connector.connect(host='localhost',user="root",password='admin')

app = Flask(__name__)
app.config['JSON_SORT_KEY'] = False

@app.route('/clientes', methods=['GET'])
def get_carros():
    return make_response(
        jsonify(
            mensagem='lista de clientes',
            dados="teste"
        )
    )

app.run()