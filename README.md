# Python Challenge 02


## Introdução

Nesse desafio trabalharemos no desenvolvimento de uma REST API para utilizar a informação do projeto Open Food Facts, que é uma base de datos aberta com informações nutricional de diversos produtos alimentícios.

O projeto tem como objetivo dar suporte a equipe de nutricionista da empresa Fitness Foods LC para que eles possam revisar de maneira rápida a informação nutriconal dos alimentos.

### Obrigatório
 
- Trabalhar em um FORK deste repositório em seu usuário;
- O projeto back-end deverá ser desenvolvido usando Python com o framework Django;
- Configurar os testes usando Pytest
- Documentação para configuração do projeto em ambientes de produção
 

## O projeto
 
- Criar um banco de dados no Mongo Atlas: https://www.mongodb.com/cloud/atlas
- Criar uma REST API usando Django com as melhores práticas de desenvolvimento
- Integrar a API com o banco de dados MongoDB criado no Atlas para persistir os dados
- Desenvolver Tests Unitários


### Modelo de Datos:

Para a definição do modelo, consultar o arquivo [products.json](./products.json) que foi exportado do Open Food Facts, um detalhe importante é temos dois novos campos para poder fazer o controle interno e que deverão ser aplicado em todos os alimentos que forem importados:

- `imported_t`, campo do tipo Date com a dia e hora que foi importado para base.
- `status`, campo do tipo Enum com os possíveis valors: draft, trash, published

### Sistema do CRON

Para proseguir com o desafio, precisaremos criar na API um sistema de atualização que vai atualizar os datos do MongoDb com a versão mais recente do [Open Food Facts](https://br.openfoodfacts.org/data).

A lista de arquivos do Open Food, pode ser encontra em: 

- https://static.openfoodfacts.org/data/delta/index.txt

Onde cada linha representa um arquivo que está disponível em https://static.openfoodfacts.org/data/delta/{filename}. O nome do arquivo contém o timestamp UNIX da primeira e última alteração contida no archivo JSON, para que os arquivos possam ser importados (após extracção) em ordem alfabética.

É recomendavél utilizar uma Collection secundária para controlar os históricos das importações e facilitar a validação durante a execução.


Nota: Importante lembrar que todos os dados deverão ter os campos personalizados `imported_t`, `status`.

### A REST API

Na REST API teremos um CRUD com os seguientes endpoints:

 - `GET /`: Detalhes da API, se conexão leitura e escritura com a base de datos está OK, horário da última vez que o CRON foi executado, tempo online e uso de memória.
 - `PUT /products/:code`: Será responsável por receber atualizações do Projeto Web
 - `DELETE /products/:code`: Mudar o status do produto para `trash`
 - `GET /products/:code`: Obter a informação somente de um produto da base de dados
 - `GET /products`: Listar todos os produtos da base de dados, adicionar sistema de paginação para não sobrecargar o `REQUEST`.

Ao terminar os endpoints, configurar os tests usando Pytest.

 
## [Bonus] Front-End
 
#### Listar alimentos
 
Criar uma sessão na tela com uma tabela para listar os alimentos processados pela API. É importante ter os seguintes campos:
 
        - Nome
        - Tipo
        - Criado
        - Ações (Botões Ver)
  
#### Ver alimentos

Para visualizar os alimentos, usaremos diretamente o projeto Open Food Facts, para isso é importante aprender a montar a URL:

- https://br.openfoodfacts.org/produto/{code}


Por exemplo:

- https://br.openfoodfacts.org/produto/0737628064502


## Readme do Repositório
 
- Deve conter o título de cada projeto
- Uma descrição de uma frase
- Como instalar e usar o projeto (instruções)
