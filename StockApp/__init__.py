import os
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_session import Session

db = SQLAlchemy()
login_manager = LoginManager()
# sess = Session()
def create_app():
    app = Flask(__name__,instance_relative_config=False,template_folder="templates")
    app.config.from_object("config.DevConfig")
    db.init_app(app)
    login_manager.init_app(app)
    # sess.init_app(app)
    CORS(app)
    with app.app_context():
        from . import routes
        from . import auth
        from . import stock

        # Register Blueprints
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(stock.stock_bp)
        db.create_all()
        return app