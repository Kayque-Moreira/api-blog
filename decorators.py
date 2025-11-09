from functools import wraps
from flask import request, jsonify
import jwt
from banco_de_dados import app, Autor


def token_obrigatorio(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Verifica se há o header Authorization
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({'mensagem': 'Token de autenticação é obrigatório!'}), 401

        # (aqui depois faremos a validação do token)

        return f(*args, **kwargs)

    return decorated
