from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ativo = db.Column(db.Boolean, nullable=False, default=True)
    data_cadastro = db.Column(db.DateTime, nullable=False, default=datetime.now)
    cpf = db.Column(db.String(11))
    nome = db.Column(db.String(120), nullable=False)
    celular = db.Column(db.String(13))
    telefone = db.Column(db.String(12))

    def serialize(self):
        return {
            'ID_CLIENTE': self.id_cliente,
            'ATIVO': self.ativo,
            'DATA_CADASTRO': self.data_cadastro.strftime('%d/%m/%Y %H:%M:%S'),  # Convertendo para formato ISO 8601
            'CPF': self.cpf,
            'NOME': self.nome,
            'CELULAR': self.celular,
            'TELEFONE': self.telefone
        }

class Motorista(db.Model):
    __tablename__ = 'motorista'
    id_motorista = db.Column(db.Integer, primary_key = True,autoincrement = True)
    ativo = db.Column(db.Boolean, nullable=False, default=True)
    data_cadastro = db.Column(db.DateTime, nullable=False, default=datetime.now)
    cpf = db.Column(db.String(11))
    nome = db.Column(db.String(120), nullable=False)
    celular = db.Column(db.String(13))
    telefone = db.Column(db.String(12))

    def serialize(self):
        return {
            'ID_MOTORISTA': self.id_motorista,
            'ATIVO': self.ativo,
            'DATA_CADASTRO': self.data_cadastro.strftime('%d/%m/%Y %H:%M:%S'),  # Convertendo para formato ISO 8601
            'CPF': self.cpf,
            'NOME': self.nome,
            'CELULAR': self.celular,
            'TELEFONE': self.telefone
        }
    

class Van(db.Model):
    __tablename__ = 'van'
    id_van = db.Column(db.Integer, primary_key = True,autoincrement = True)
    ativo = db.Column(db.Boolean, nullable=False, default=True)
    data_cadastro = db.Column(db.DateTime, nullable=False, default=datetime.now)
    id_motorista = db.Column(db.Integer, db.ForeignKey('Motorista.id_motorista'), nullable=False)
    placa = db.Column(db.String(7), nullable=False)
    modelo = db.Column(db.String(70))
    km_atual = db.Column(db.Float)

    #relações
    motorista = db.relationship('Motorista', foreign_keys=[id_motorista], backref=db.backref('van', lazy='dynamic'), primaryjoin="Van.id_motorista == Motorista.id_motorista")

    def serialize(self):
        return {
            'ID_VAN': self.id_van,
            'ATIVO': self.ativo,
            'DATA_CADASTRO': self.data_cadastro.strftime('%d/%m/%Y %H:%M:%S'),  # Convertendo para formato ISO 8601
            'ID_MOTORISTA': self.id_motorista,
            'MOTORISTA': self.motorista.nome,
            'MODELO': self.modelo,
            'KM_ATUAL': self.km_atual
        }


class Categoria(db.Model):
    __tablename__ = 'categoria'
    id_categoria = db.Column(db.Integer, primary_key = True, autoincrement = True)
    descricao = db.Column(db.String(80), nullable=False)
    tipo_categoria = db.Column(db.Enum('despesa','receita'), nullable=False)

    def serialize(self):
        return{
            'ID_CATEGORIA':self.id_categoria,
            'DESCRICAO': self.descricao,
            'TIPO_CATEGORIA': self.tipo_categoria
        }

class FormasPagamento(db.Model):
    __tablename__ = 'formas_pagamento'
    id_pagamento = db.Column(db.Integer, primary_key=True,autoincrement = True)
    descricao = db.Column(db.String(60), nullable=False)

    def serialize(self):
        return{
            'ID_PAGAMENTO': self.id_pagamento,
            'DESCRICAO': self.descricao
        }
    
class ContasReceber(db.Model):
    __tablename__ =  'contas_receber'
    #Colunas da tabela contas pagar
    id_contas_receber = db.Column(db.Integer, primary_key=True,autoincrement = True)
    id_cliente = db.Column(db.Integer, nullable=False)
    id_categoria = db.Column(db.Integer, nullable=False)
    id_pagamento = db.Column(db.Integer, nullable=False)
    data_cadastro = db.Column(db.DateTime, nullable=False, default=datetime.now)
    data_vencimento = db.Column(db.DateTime, nullable=False)
    data_recebimento = db.Column(db.Date)
    descricao = db.Column(db.String(120))
    valor_titulo = db.Column(db.Numeric(precision=10,scale=3), nullable=False)
    valor_pago = db.Column(db.Numeric(precision=10, scale=3))
    status_titulo = db.Column(db.Enum('em aberto','quitado'), nullable=False)

    #relações
    cliente = db.relationship('Cliente', foreign_keys=[id_cliente], backref=db.backref('ContasReceber', lazy='dynamic'), primaryjoin="ContasReceber.id_cliente == Cliente.id_cliente")
    categoria = db.relationship('Categoria', foreign_keys=[id_categoria], backref=db.backref('ContasReceber', lazy='dynamic'), primaryjoin="ContasReceber.id_categoria == Categoria.id_categoria")
    pagamento = db.relationship('FormasPagamento', foreign_keys=[id_pagamento], backref=db.backref('ContasReceber', lazy='dynamic'), primaryjoin="ContasReceber.id_pagamento == FormasPagamento.id_pagamento")

    def serialize(self):
        return{
            'ID_CONTAS_RECEBER': self.id_contas_receber,
            'DATA_CADASTRO': self.data_cadastro.strftime('%d/%m/%Y %H:%M:%S'), 
            'STATUS_TITULO': self.status_titulo,
            'ID_CLIENTE': self.id_cliente,
            'NOME': self.cliente.nome,
            'ID_CATEGORIA': self.id_categoria,
            'CATEGORIA': self.categoria.descricao,
            'DESCRICAO': self.descricao,
            'DATA_VENCIMENTO': self.data_vencimento.strftime('%d/%m/%Y'),
            'VALOR_TITULO': float(self.valor_titulo),
            'VALOR_PAGO' : float(self.valor_pago) if self.valor_pago is not None else None,
            'DATA_RECEBIMENTO': self.data_recebimento.strftime('%d/%m/%Y') if self.data_recebimento is not None else None,
            'ID_PAGAMENTO': self.id_pagamento,
            'PAGAMENTO': self.pagamento.descricao
            
        }

class ContasPagar(db.Model):
    __tablename__ =  'contas_pagar'
    #Colunas da tabela contas pagar
    id_contas_pagar = db.Column(db.Integer, primary_key=True,autoincrement = True)
    id_van = db.Column(db.Integer, nullable=False)
    id_categoria = db.Column(db.Integer, nullable=False)
    id_pagamento = db.Column(db.Integer, nullable=False)
    data_cadastro = db.Column(db.DateTime, nullable=False, default=datetime.now)
    data_vencimento = db.Column(db.DateTime, nullable=False)
    data_pagamento = db.Column(db.Date)
    descricao = db.Column(db.String(120))
    valor_titulo = db.Column(db.Numeric(precision=10,scale=3), nullable=False)
    valor_pago = db.Column(db.Numeric(precision=10, scale=3))
    status_titulo = db.Column(db.Enum('em aberto','quitado'), nullable=False)

    #relações
    van = db.relationship('Van', foreign_keys=[id_van], backref=db.backref('ContasPagar', lazy='dynamic'), primaryjoin="ContasPagar.id_van == Van.id_van")
    categoria = db.relationship('Categoria', foreign_keys=[id_categoria], backref=db.backref('ContasPagar', lazy='dynamic'), primaryjoin="ContasPagar.id_categoria == Categoria.id_categoria")
    pagamento = db.relationship('FormasPagamento', foreign_keys=[id_pagamento], backref=db.backref('ContasPagar', lazy='dynamic'), primaryjoin="ContasPagar.id_pagamento == FormasPagamento.id_pagamento")

    def serialize(self):
        return{
            'ID_CONTAS_PAGAR': self.id_contas_pagar,
            'DATA_CADASTRO': self.data_cadastro.strftime('%d/%m/%Y %H:%M:%S'), 
            'STATUS_TITULO': self.status_titulo,
            'ID_VAN': self.id_van,
            'PLACA': self.van.placa,
            'MOTORISTA' : self.van.motorista.nome,
            'ID_CATEGORIA': self.id_categoria,
            'CATEGORIA': self.categoria.descricao,
            'DESCRICAO': self.descricao,
            'DATA_VENCIMENTO': self.data_vencimento.strftime('%d/%m/%Y'),
            'VALOR_TITULO': float(self.valor_titulo),
            'VALOR_PAGO' : float(self.valor_pago) if self.valor_pago is not None else None,
            'DATA_PAGAMENTO': self.data_pagamento.strftime('%d/%m/%Y') if self.data_pagamento is not None else None,
            'ID_PAGAMENTO': self.id_pagamento,
            'PAGAMENTO': self.pagamento.descricao
            
        }