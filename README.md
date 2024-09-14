# Tutorial com Flask e PostgreSQL

Esse tutorial mostra como fazer um crud simples usando a arquitetura MVC com Singleton.

As pastas estão organizadas de acordo com a responsabilidade de cada módulo.
- Na pasta controller há somente arquivos relacionados com os controladores. Já que temos apenas o pesquisador como entidade nesse tutorial, temos somente controladores relacionados com ele.
 - Dentro da pasta controller também tem a pasta dao (Data Access Object), que tem somente código relacionado com a interação com o banco de dados.
- Na pasta model temos a classe da entidade Pesquisador  
