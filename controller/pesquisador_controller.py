from flask import Blueprint, jsonify, request
from controller.dao.pesquisador_dao import apagar_por_lattes_id, listar_todos, salvar_novo_pesquisador, atualizar_por_id

# Criação de um Blueprint chamado 'pesquisador_controller'
pesquisador_controller = Blueprint('pesquisador_controller', __name__)

# Rota para salvar um novo pesquisador
@pesquisador_controller.route("/pesquisadores", methods=["POST"])
def adicionar() -> str:
    # Pega o JSON enviado na requisição
    dados = request.get_json()
    
    # Obtém os valores dos campos do JSON
    nome = dados.get('nome')
    lattes_id = dados.get('lattes_id')
    id = dados.get('pesquisadores_id')
    
    # Verifica se todos os campos obrigatórios foram informados
    if nome is None:
        return jsonify({'erro': 'O campo nome deve ser informado.'}), 400

    if lattes_id is None:
        return jsonify({'erro': 'O campo lattes_id deve ser informado.'}), 400

    if id is None:
        return jsonify({'erro': 'O campo pesquisadores_id deve ser informado.'}), 400

    # Chama a função para salvar o novo pesquisador
    resposta = salvar_novo_pesquisador(nome, lattes_id, id)
    
    # Retorna a resposta como JSON
    return jsonify(resposta)
    

# Rota para listar todos os pesquisadores
@pesquisador_controller.route("/pesquisadores", methods=["GET"])
def listar() -> str:
    # Chama a função para listar todos os pesquisadores
    lista_todos_pesquisadores = listar_todos()

    # Retorna a lista de pesquisadores como JSON
    return jsonify(lista_todos_pesquisadores)

# Rota para apagar um pesquisador com base no lattes_id
@pesquisador_controller.route("/pesquisadores/<string:lattes_id>", methods=["DELETE"])
def apagar(lattes_id: str) -> str:
    # Chama a função para apagar um pesquisador pelo lattes_id
    resposta = apagar_por_lattes_id(lattes_id)
    
    # Retorna a resposta como JSON
    return jsonify(resposta)

# Rota para atualizar um pesquisador com base no lattes_id
@pesquisador_controller.route("/pesquisadores/<string:lattes_id>", methods=["PUT"])
def atualizar(lattes_id: str) -> str:
    # Pega o JSON enviado na requisição
    dados = request.get_json()
    
    # Obtém os valores dos campos do JSON
    lattes_id = dados.get('lattes_id')
    nome = dados.get('nome')
    pesquisadores_id = dados.get('pesquisadores_id')
    
    # Chama a função para atualizar o pesquisador
    resposta = atualizar_por_id(nome, pesquisadores_id, lattes_id)
    
    # Retorna a resposta como JSON
    return jsonify(resposta)
