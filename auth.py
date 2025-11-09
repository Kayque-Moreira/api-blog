from flask import Blueprint, jsonify, request
from banco_de_dados import app, db, Autor
import jwt
from datetime import datetime, timedelta

auth = Blueprint('auth', __name__)




@auth.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    email = dados.get('email')
    senha = dados.get('senha')

    autor = Autor.query.filter_by(email=email, senha=senha).first()

    if not autor:
        return jsonify({'mensagem': 'Credenciais inválidas'}), 401
    
# Gerar o token com expiração de 30 minutos
    payload = {
        'id_autor': autor.id_autor,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({
        'mensagem': 'Login realizado com sucesso!',
        'token': token
})
