# Tutorial com Flask e PostgreSQL

Esse tutorial mostra como fazer um crud simples usando a arquitetura MVC com Singleton.

As pastas estão organizadas de acordo com a responsabilidade de cada módulo.
- Na pasta controller há somente arquivos relacionados com os controladores. Já que temos apenas o pesquisador como entidade nesse tutorial, temos somente controladores relacionados com ele.
 - Dentro da pasta controller também tem a pasta dao (Data Access Object), que tem somente código relacionado com a interação com o banco de dados.
- Na pasta model temos a classe da entidade Pesquisador

_____________________________________________________________

__> Antes de começar verifique se você tem a versão do Python acima da 3.12 e o Docker instalado.__

### Passo 1

Rode o comando **git clone <endereco_do_repositorio>** na pasta desejada

### Passo 2 

Crie um ambiente virtual python para não misturar as dependências desse tutorial com as bibliotecas instaladas globalmente no computador.

` python -m venv <nome_do_venv> `

### Passo 3

Depois de criar o ambiente virtual, rode o seguinte comando no terminal:

 ##### No Linux

` source nome_do_ambiente/bin/activate `

 ##### No Windows

` nome_do_ambiente\Scripts\activate.bat `

### Passo 4

Rode o arquivo `povoar_bd.py` para colocar os dados dos pesquisadores para teste no banco.

### Passo 5

Rode o arquivo `app.py` e faça as requisições GET, POST, PUT e DELETE para /pesquisadores para testar.
A aplicação estará rodando na porta 5000. Digite `http://localhost:5000` no navegador.

