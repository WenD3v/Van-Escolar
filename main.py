import mysql.connector
from flask import Flask, make_response, jsonify, request

mydb = mysql.connector.connect(host='localhost',user="root",password='admin',database='van')

app = Flask(__name__)
app.debug = True
app.config['JSON_SORT_KEY'] = False

def execute_query(query):
    # Função para executar consultas
    try:
        mydb = mysql.connector.connect(host='localhost',user="root",password='admin',database='van')
        my_cursor = mydb.cursor(dictionary=True)
        my_cursor.execute(query)
        columns = [column[0] for column in my_cursor.description]
        result = my_cursor.fetchall()
        data = [dict(zip(columns,row)) for row in result]
        my_cursor.close()
        mydb.close()
        return data
    except mysql.connector.Error as err:
        return {'error':f'Erro ao executar a consulta: {err}'}

@app.route('/clientes', methods=['GET'])
def get_carros():
    
    query="select id_cliente, ativo, data_cadastro, cpf, nome, celular, telefone from cliente"
    data = execute_query(query)
    if 'error' in data:
        return jsonify(data), 500
    else:
        return make_response(
            jsonify(
                data
            )
        )

@app.route('/motoristas', methods=['GET'])
def get_motoristas():
    query="""
    select id_motorista, ativo, data_cadastro, cpf, nome, celular, telefone from motorista
    """
    data = execute_query(query)
    if 'error' in data:
        return jsonify(data),500
    else:
        return make_response(
            jsonify(
                data
            )
        )

@app.route('/vans', methods=['GET'])
def get_vans():
    
    query="""
        select V.id_van, V.ativo, V.data_cadastro, V.id_motorista, M.nome as motorista, V.placa, V.modelo, V.km_atual from Van as V
        inner join motorista as M on M.id_motorista = V.id_motorista
    """
    data = execute_query(query)
    if 'error' in data:
        return jsonify(data),500
    else:
        return make_response(
            jsonify(
                data
            )
        )

@app.route('/categorias', methods=['GET'])
def get_categorias():
    
    query="select id_categoria, descricao, tipo_categoria from categoria order by id_categoria"
    data=execute_query(query)
    if 'error' in data:
        return jsonify(data),500
    else:
        return make_response(
            jsonify(
                data
            )
        )

@app.route('/contas_receber',methods=['GET'])
def get_contas_receber():

    query="""
        select T.status_titulo as status, T.Id_contas_receber, C.nome as cliente, Cat.descricao as categoria, T.descricao,T.Data_Vencimento, T.Valor_titulo, T.Valor_Pago,T.Data_recebimento, P.descricao as pagamento  from Contas_receber as T
        inner join Cliente as C on C.Id_Cliente = T.Id_cliente
        inner join Categoria as Cat on Cat.id_categoria = T.id_categoria
        inner join Formas_pagamento as P on P.id_pagamento = T.id_pagamento
        order by T.Data_vencimento;
    """
    data=execute_query(query)
    if 'error' in data:
        return jsonify(data),500
    else:
        return make_response(
            jsonify(
                data
            )
        )

@app.route('/contas_receber/quitados',methods=['GET'])
def get_contas_receber_quitados():

    query = """"
        select T.Id_contas_receber, C.nome as cliente, Cat.descricao as categoria, T.descricao,T.Data_vencimento, T.Valor_titulo, T.Valor_Pago,T.Data_Recebimento, P.descricao as pagamento  from Contas_receber as T
        inner join Cliente as C on C.Id_Cliente = T.Id_cliente
        inner join Categoria as Cat on Cat.id_categoria = T.id_categoria
        inner join Formas_pagamento as P on P.id_pagamento = T.id_pagamento
        where T.status_titulo = 'quitado'
        order by T.Data_Vencimento;
    """
    data = execute_query(query)
    if 'error' in data:
        return jsonify(data),500
    else:
        return make_response(
            jsonify(
                data
            )
        )

@app.route('/contas_receber/abertos',methods=['GET'])
def get_contas_receber_abertos():
    my_cursor = mydb.cursor()
    my_cursor.execute("""
        select T.Id_contas_receber, C.nome as cliente, Cat.descricao as categoria, T.descricao,T.Data_vencimento, T.Valor_titulo, T.Valor_Pago,T.Data_Recebimento, P.descricao as pagamento  from Contas_receber as T
        inner join Cliente as C on C.Id_Cliente = T.Id_cliente
        inner join Categoria as Cat on Cat.id_categoria = T.id_categoria
        inner join Formas_pagamento as P on P.id_pagamento = T.id_pagamento
        where T.status_titulo = 'em aberto'
        order by T.Data_Vencimento;
    """)
    columns = [column[0] for column in my_cursor.description]
    minhas_contas = my_cursor.fetchall()
    data = [dict(zip(columns,row)) for row in minhas_contas]
    my_cursor.close()
    if 'error' in data:
        return jsonify(data),500
    else:
        return make_response(
            jsonify(
                data
            )
        )

@app.route('/contas_pagar',methods=['GET'])
def get_contas_pagar():
    my_cursor = mydb.cursor()
    my_cursor.execute("""
        select T.Status_titulo as status, T.Id_contas_pagar, V.placa, Cat.descricao as categoria, T.descricao,T.Data_vencimento, T.Valor_titulo, T.Valor_Pago,T.Data_Pagamento, P.descricao as pagamento  from Contas_Pagar as T
        inner join Van as V on V.Id_Van = T.ID_van
        inner join Categoria as Cat on Cat.id_categoria = T.id_categoria
        inner join Formas_pagamento as P on P.id_pagamento = T.id_pagamento
        order by T.Data_vencimento;
    """)
    columns = [column[0] for column in my_cursor.description]
    minhas_contas = my_cursor.fetchall()
    data = [dict(zip(columns,row)) for row in minhas_contas]
    my_cursor.close()
    if 'error' in data:
        return jsonify(data),500
    else:
        return make_response(
            jsonify(
                data
            )
        )

@app.route('/contas_pagar/quitados',methods=['GET'])
def get_contas_pagar_quitados():
    my_cursor = mydb.cursor()
    my_cursor.execute("""
        select T.Id_contas_pagar, V.placa, Cat.descricao as categoria, T.descricao,T.Data_vencimento, T.Valor_titulo, T.Valor_Pago,T.Data_pagamento, P.descricao as pagamento  from Contas_Pagar as T
        inner join Van as V on V.Id_Van = T.ID_van
        inner join Categoria as Cat on Cat.id_categoria = T.id_categoria
        inner join Formas_pagamento as P on P.id_pagamento = T.id_pagamento
        where T.status_titulo = 'quitado'
        order by T.data_vencimento;
    """)
    columns = [column[0] for column in my_cursor.description]
    minhas_contas = my_cursor.fetchall()
    data = [dict(zip(columns,row)) for row in minhas_contas]
    my_cursor.close()
    if 'error' in data:
        return jsonify(data),500
    else:
        return make_response(
            jsonify(
                data
            )
        )

@app.route('/contas_pagar/abertos',methods=['GET'])
def get_contas_pagar_abertos():
    my_cursor = mydb.cursor()
    my_cursor.execute("""
        select T.Id_contas_pagar, V.placa, Cat.descricao as categoria, T.descricao,T.Data_vencimento, T.Valor_titulo, T.Valor_Pago,T.Data_pagamento, P.descricao as pagamento  from Contas_Pagar as T
        inner join Van as V on V.Id_Van = T.ID_van
        inner join Categoria as Cat on Cat.id_categoria = T.id_categoria
        inner join Formas_pagamento as P on P.id_pagamento = T.id_pagamento
        where T.status_titulo = 'em aberto'
        order by T.data_vencimento;
    """)
    columns = [column[0] for column in my_cursor.description]
    minhas_contas = my_cursor.fetchall()
    data = [dict(zip(columns,row)) for row in minhas_contas]
    my_cursor.close()
    if 'error' in data:
        return jsonify(data),500
    else:
        return make_response(
            jsonify(
                data
            )
        )

if __name__ == '__main__':
    # Permite conexões de outros dispositivos na rede
    app.run(host='0.0.0.0', port=5000)