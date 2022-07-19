# Desafio:

Construa uma aplicação usando a linguagem Python, para ser um repositório de jogos de computador (um lugar para armazenar jogos de computador).

Para isso: 
- Construa uma classe chamada jogos, que devera ter as propriedades:
  - Nome,
  - Id (identificador)
  - Descrição,
  - Ano de lançamento, e
  - Fabricante
- Construa 5 métodos dentro dessa classe:
  - salvar() (armazena um jogo)
  - listar() (lista todos os jogos de uma instância ou objeto)
  - listar(id_jogo) (lista apenas um jogo)
  - deletar(id_jogo) (deleta apenas um jogo)
  - atualizar(id_jogo) (atualiza um único jogo) 
- Crie uma instância da classe e salve no mínimo 5 jogos
- Cada instância deverá criar seu próprio arquivo de banco de dados
  
**importante**: 
- salve os dados em um documento .txt chamado de banco_de_dados
- os dados não poderão ser perdidos, de modo que quando alguém usar o método Listar(), todos os jogos 
  salvos deverão ser retornados

