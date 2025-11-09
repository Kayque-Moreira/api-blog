from flask import Flask
from banco_de_dados import app, db
from auth import auth
from postagens import postagens_bp
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'FDSDSY7A98D'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Registrando os blueprints
app.register_blueprint(postagens_bp)
# Registrar o blueprint de autenticação
app.register_blueprint(auth, url_prefix='/auth')

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
