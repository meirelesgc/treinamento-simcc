from flask import Blueprint, jsonify, request
from controller.dao.pesquisador_dao import apagar_por_lattes_id, listar_todos, salvar_novo_pesquisador, atualizar_por_id
from pydantic import ValidationError
from controller.modelo_pydantic.modelo import PesquisadorSchema  # Importa o modelo Pydantic
from flasgger import swag_from

# Criação de um Blueprint chamado 'pesquisador_controller'
pesquisador_controller = Blueprint('pesquisador_controller', __name__)

# Rota para salvar um novo pesquisador
@pesquisador_controller.route("/pesquisadores", methods=["POST"])
@swag_from({
    'responses': {
        200: {
            'description': 'Pesquisador salvo com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'lattes_id': {'type': 'string'},
                    'pesquisadores_id': {'type': 'string'}
                }
            }
        },
        400: {
            'description': 'Dados inválidos'
        }
    },
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'id': 'Pesquisador',
                'required': ['nome', 'lattes_id', 'pesquisadores_id'],
                'properties': {
                    'nome': {'type': 'string'},
                    'lattes_id': {'type': 'string'},
                    'pesquisadores_id': {'type': 'string'}
                }
            }
        }
    ]
})
def adicionar() -> str:
    try:
        # Pega o JSON enviado na requisição e valida com Pydantic
        dados = request.get_json()
        pesquisador = PesquisadorSchema(**dados)
        
        # Chama a função para salvar o novo pesquisador passando os dados validados
        resposta = salvar_novo_pesquisador(
            nome=pesquisador.nome,
            lattes_id=pesquisador.lattes_id,
            pesquisadores_id=pesquisador.pesquisadores_id
        )
        
        # Retorna a resposta como JSON
        return jsonify(resposta)
    
    except ValidationError as e:
        # Retorna o erro de validação como JSON, com código de erro 400
        return jsonify({"erro": e.errors()}), 400


# Rota para listar todos os pesquisadores
@pesquisador_controller.route("/pesquisadores", methods=["GET"])
@swag_from({
    'responses': {
        200: {
            'description': 'Lista de todos os pesquisadores',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'nome': {'type': 'string'},
                        'lattes_id': {'type': 'string'},
                        'pesquisadores_id': {'type': 'string'}
                    }
                }
            }
        }
    }
})
def listar() -> str:
    # Chama a função para listar todos os pesquisadores
    lista_todos_pesquisadores = listar_todos()

    # Retorna a lista de pesquisadores como JSON
    return jsonify(lista_todos_pesquisadores)


# Rota para apagar um pesquisador com base no lattes_id
@pesquisador_controller.route("/pesquisadores/<string:lattes_id>", methods=["DELETE"])
@swag_from({
    'responses': {
        200: {
            'description': 'Pesquisador apagado com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        }
    },
    'parameters': [
        {
            'name': 'lattes_id',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'ID do Lattes do pesquisador'
        }
    ]
})
def apagar(lattes_id: str) -> str:
    # Chama a função para apagar um pesquisador pelo lattes_id
    resposta = apagar_por_lattes_id(lattes_id)
    
    # Retorna a resposta como JSON
    return jsonify(resposta)


# Rota para atualizar um pesquisador com base no lattes_id
@pesquisador_controller.route("/pesquisadores/<string:lattes_id>", methods=["PUT"])
@swag_from({
    'responses': {
        200: {
            'description': 'Pesquisador atualizado com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'lattes_id': {'type': 'string'},
                    'pesquisadores_id': {'type': 'string'}
                }
            }
        },
        400: {
            'description': 'Erro de validação'
        }
    },
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'id': 'Pesquisador',
                'required': ['nome', 'lattes_id', 'pesquisadores_id'],
                'properties': {
                    'nome': {'type': 'string'},
                    'lattes_id': {'type': 'string'},
                    'pesquisadores_id': {'type': 'string'}
                }
            }
        }
    ]
})
def atualizar(lattes_id: str) -> str:
    try:
        # Pega o JSON enviado na requisição e valida com Pydantic
        dados = request.get_json()
        pesquisador = PesquisadorSchema(**dados)
        
        # Chama a função para atualizar o pesquisador
        resposta = atualizar_por_id(
            nome=pesquisador.nome,
            pesquisadores_id=pesquisador.pesquisadores_id,
            lattes_id=pesquisador.lattes_id
        )
        
        # Retorna a resposta como JSON
        return jsonify(resposta)
    
    except ValidationError as e:
        # Retorna o erro de validação como JSON, com código de erro 400
        return jsonify({"erro": e.errors()}), 400
