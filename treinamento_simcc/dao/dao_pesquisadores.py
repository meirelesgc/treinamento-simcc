import pandas as pd
from dao import banco

from pprint import pprint
from model.pesquisador import Pesquisador


def consultar_pesquisadores():
    script_sql = """
        SELECT
            pesquisadores_id, 
            lattes_id, 
            nome
        FROM 
            pesquisadores;
        """

    registro = banco.select(script_sql)

    # Só pra saber como chega o registro do banco
    pprint(registro)

    df = pd.DataFrame(registro, columns=["pesquisadores_id", "lattes_id", "nome"])

    lista_de_pesquisadores = list()
    for index, dados in df.iterrows():
        print(dados)
        pesquiasdor = Pesquisador()
        pesquiasdor.pesquisadores_id = dados["pesquisadores_id"]
        pesquiasdor.lattes_id = dados["lattes_id"]
        pesquiasdor.nome = dados["nome"]

        lista_de_pesquisadores.append(pesquiasdor.gerar_json())

    return lista_de_pesquisadores
