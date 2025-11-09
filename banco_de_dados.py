from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instância do Flask
app = Flask(__name__)

# Configurações
app.config['SECRET_KEY'] = 'FDSDSY7A98D'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # evita warning

# Instância do SQLAlchemy
db = SQLAlchemy(app)

# Classes Autor e Postagem
# Classe Postagem
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))
    conteudo = db.Column(db.Text)

# Classe Autor

class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(50))
    admin = db.Column(db.Boolean, default=False)
    postagens = db.relationship('Postagem')

# Inicializar o banco de dados
def inicializar_banco():
    with app.app_context():
        db.drop_all()
        db.create_all()

# Criar um usuário Admin
        autor = Autor(nome='w1eak', email='w1eak@email.com', senha='123456', admin=True)
        db.session.add(autor)
        db.session.commit()

# Garantir inicialização do banco de dados
if __name__ == "__main__":
    inicializar_banco()