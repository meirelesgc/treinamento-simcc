from flask import Flask
from flasgger import Swagger
from controller.pesquisador_controller import pesquisador_controller

app = Flask(__name__)

# Configura o Swagger
swagger = Swagger(app)

@app.route("/", methods=["GET"])
def index():
    return """
        <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tutorial inicial</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            background-image: linear-gradient(306deg, rgba(54, 54, 54, 0.05) 0%, rgba(54, 54, 54, 0.05) 33.333%,rgba(85, 85, 85, 0.05) 33.333%, rgba(85, 85, 85, 0.05) 66.666%,rgba(255, 255, 255, 0.05) 66.666%, rgba(255, 255, 255, 0.05) 99.999%),linear-gradient(353deg, rgba(81, 81, 81, 0.05) 0%, rgba(81, 81, 81, 0.05) 33.333%,rgba(238, 238, 238, 0.05) 33.333%, rgba(238, 238, 238, 0.05) 66.666%,rgba(32, 32, 32, 0.05) 66.666%, rgba(32, 32, 32, 0.05) 99.999%),linear-gradient(140deg, rgba(192, 192, 192, 0.05) 0%, rgba(192, 192, 192, 0.05) 33.333%,rgba(109, 109, 109, 0.05) 33.333%, rgba(109, 109, 109, 0.05) 66.666%,rgba(30, 30, 30, 0.05) 66.666%, rgba(30, 30, 30, 0.05) 99.999%),linear-gradient(189deg, rgba(77, 77, 77, 0.05) 0%, rgba(77, 77, 77, 0.05) 33.333%,rgba(55, 55, 55, 0.05) 33.333%, rgba(55, 55, 55, 0.05) 66.666%,rgba(145, 145, 145, 0.05) 66.666%, rgba(145, 145, 145, 0.05) 99.999%),linear-gradient(90deg, rgb(9, 201, 186),rgb(18, 131, 221));
        }
    </style>
</head>
<body>
    <div style="width: 90%; margin: auto;">
        <p style="font-size: 25px; text-align: center; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif">
            Agora que está tudo pronto você poderá testar a aplicação CRUD!
        </p>
        <p style="background-color: rgba(38, 232, 80, 0.7); padding: 20px; box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.363); border-radius: 10px; font-size: 20px; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif">
            Este tutorial é uma aplicação de um CRUD (Create, Read, Update, Delete) simples com API documentada.<br /><br />
            Clique <a style="color: blue; text-decoration: none; background-color: white; padding: 5px 8px; border-radius: 5px;" href="http://localhost:5000/apidocs">AQUI</a> para acessar a documentação.
        </p>
        <p style="padding: 20px; font-size: 18px; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; background-color:rgba(246, 255, 0, 0.7); border-radius: 10px; box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.363);">
            Já estão salvos no banco uma lista de pesquisadores que você adicionou quando rodou o script <span style="background-color: rgba(183, 183, 183, 0.796); border-radius: 3px; padding: 3px; font-family: 'Courier New', Courier, monospace;">povoar_bd.py</span>. Você consegue ver o json normalmente digitando no navegador: <a style="display: block; margin: 20px;;" href="http://localhost:5000/pesquisadores">http://localhost:5000/pesquisadores</a>Mas para adicionar um novo pesquidor, atualizar ou excluir, use o ThunderClient ou PostMan (Extensões no VSCode).
        </p>
        <p style="padding: 20px; font-size: 18px; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; background-color:rgba(255, 247, 0, 0.7); border-radius: 10px; box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.363);">
            O campo <i>pesquisadores_id</i> tem um formato que você pode gerar <a href="https://www.uuidgenerator.net/version4" target="_blank">aqui.</a><br />
            Sem esse formato não é possível adicionar um novo pesquisador. Basta só gerar, copiar e colar.
        </p>
        
    </div>
</body>
</html>
    """


@app.route("/test", methods=["GET"])
def test():
    return "API is working!"


# Registra o Blueprint do controlador de pesquisadores
app.register_blueprint(pesquisador_controller)

if __name__ == "__main__":
    app.run(debug=True)
