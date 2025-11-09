from flask import Blueprint, jsonify, request
from banco_de_dados import db, Postagem
from decorators import token_obrigatorio

postagens_bp = Blueprint('postagens', __name__, url_prefix='/postagens')


@postagens_bp.route('/', methods=['GET'])
@token_obrigatorio
def listar_postagens():
    postagens = Postagem.query.all()
    lista = []
    for p in postagens:
        lista.append({
            'id_postagem': p.id_postagem,
            'titulo': p.titulo,
            'conteudo': p.conteudo,
            'id_autor': p.id_autor
        })
    return jsonify(lista), 200


@postagens_bp.route('/<int:id_postagem>', methods=['GET'])
@token_obrigatorio
def obter_postagem(id_postagem):
    postagem = Postagem.query.get(id_postagem)
    if not postagem:
        return jsonify({'mensagem': 'Postagem não encontrada.'}), 404

    return jsonify({
        'id_postagem': postagem.id_postagem,
        'titulo': postagem.titulo,
        'conteudo': postagem.conteudo,
        'id_autor': postagem.id_autor
    }), 200


@postagens_bp.route('/', methods=['POST'])
@token_obrigatorio
def criar_postagem():
    criar_postagem = request.get_json()
    postagem = Postagem(id_autor=criar_postagem['id_autor'], titulo=criar_postagem['titulo'], conteudo=criar_postagem['conteudo'])

    db.session.add(postagem)
    db.session.commit()

    return jsonify({'Mensagem': 'Postagem criada com sucesso!'})


@postagens_bp.route('/<int:id_postagem>', methods=['PUT'])
@token_obrigatorio
def atualizar_postagem(id_postagem):
    dados = request.get_json()
    postagem = Postagem.query.filter_by(id_postagem=id_postagem).first()

    if not postagem:
        return jsonify({'mensagem': 'Esta postagem não foi encontrada'}), 404

    try:
        if 'titulo' in dados:
            postagem.titulo = dados['titulo']
        if 'conteudo' in dados:
            postagem.conteudo = dados['conteudo']
        if 'id_autor' in dados:
            postagem.id_autor = dados['id_autor']

        db.session.commit()  # 🔹 salva alterações no banco

        return jsonify({'mensagem': 'Postagem atualizada com sucesso!',}), 200  # 🔹 sempre retorne algo
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': f'Erro ao atualizar: {str(e)}'}), 500


@postagens_bp.route('/<int:id_postagem>', methods=['DELETE'])
@token_obrigatorio
def excluir_postagem(id_postagem):
    postagem_existente = Postagem.query.filter_by(id_postagem=id_postagem).first()
    if not postagem_existente:
        return jsonify({'Mensagem': 'Esta postagem não foi encontrada!'})
    db.session.delete(postagem_existente)
    db.session.commit()

    return jsonify({'Mensagem': 'Postagem excluída com sucesso!'})