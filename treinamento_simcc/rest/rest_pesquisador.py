from flask import jsonify, Blueprint
from dao import dao_pesquisadores


rest_pesquisador = Blueprint("rest_pesquisador", __name__)


@rest_pesquisador.route("/pesquisador", methods=["GET"])
def consultar_pesquisadores():
    lista = dao_pesquisadores.consultar_pesquisadores()
    return jsonify(lista)
