from flask import Flask
from .models import db
from app.blueprints.clientes import clientes_bp
from app.blueprints.motoristas import motoristas_bp
from app.blueprints.vans import vans_bp
from app.blueprints.categorias import categorias_bp
from app.blueprints.pagamentos import pagamentos_bp
from app.blueprints.contasreceber import contasreceber_bp
from app.blueprints.contaspagar import contaspagar_bp
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['JSON_SORT_KEY'] = False
    db.init_app(app)
    app.register_blueprint(clientes_bp)
    app.register_blueprint(motoristas_bp)
    app.register_blueprint(vans_bp)
    app.register_blueprint(categorias_bp)
    app.register_blueprint(pagamentos_bp)
    app.register_blueprint(contasreceber_bp)
    app.register_blueprint(contaspagar_bp)
    return app