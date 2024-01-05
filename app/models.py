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
            'id_pagamento': self.id_pagamento,
            'descricao': self.descricao
        }