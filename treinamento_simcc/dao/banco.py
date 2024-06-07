import psycopg2


def conector():
    user = "postgres"
    database = "postgres"
    password = "root"
    host = "localhost"

    conexcao = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
    )
    return conexcao


def exec(script_sql):
    conexao = conector()
    cursor = conexao.cursor()
    try:
        cursor.execute(script_sql)
        conexao.commit()
    except Exception as error:
        print(f"[Error] - {error}")
        conexao.rollback()
        cursor.close()
        return ...
    finally:
        cursor.close()


def select(script_sql):
    try:
        conexao = conector()
        cur = conexao.cursor()
        cur.execute(script_sql)
        resultado = cur.fetchall()
        conexao.close()
        cur.close()
        return resultado
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conexao.rollback()
        cur.close()
