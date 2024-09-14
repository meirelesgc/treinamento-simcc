from flask import Flask

# Importa o blueprint do módulo 'controller', especificamente o 'pesquisador_controller'
from controller.pesquisador_controller import pesquisador_controller

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Registra o blueprint 'pesquisador_controller' com a aplicação Flask
# Isso permite que as rotas definidas no blueprint estejam disponíveis na aplicação principal
app.register_blueprint(pesquisador_controller)

# Define a rota para a URL raiz ("/")
# Esta função é chamada quando um usuário acessa a URL raiz da aplicação
@app.route("/")
def index() -> str:
    return "Index"

# Define uma rota adicional para a URL "/teste"
# Esta função é chamada quando um usuário acessa a URL "/teste"
@app.route("/teste")
def teste() -> str:
    return "Teste"
    
# Executa a aplicação Flask apenas se este script for executado diretamente
# Isso é útil para evitar a execução do servidor ao importar este módulo em outro lugar
if __name__ == "__main__":
    # Inicia o servidor Flask em modo de depuração (debug)
    # O modo de depuração permite exibir mensagens detalhadas sobre erros e reiniciar o servidor automaticamente
    app.run(debug=True)
