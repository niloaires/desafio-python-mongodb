# Python Challenge (Back-End Focus)


## Introdução

Nesse desafio trabalharemos no desenvolvimento de uma REST API para utilizar os dados do projeto Open Food Facts, que é um banco de dados aberto com informação nutricional de diversos produtos alimentícios.

O projeto tem como objetivo dar suporte a equipe de nutricionistas da empresa Fitness Foods LC para que eles possam revisar de maneira rápida a informação nutricional dos alimentos que os usuários enviam pela aplicação móvel.

### Obrigatório
 
- Trabalhar em um FORK deste repositório em seu usuário;
- O projeto back-end deverá ser desenvolvido usando Python com o framework Django;
- Configurar os testes usando Pytest;
- Documentação para configuração do projeto em ambientes de produção;
 

## O projeto
 
- Criar um banco de dados no Mongo Atlas: https://www.mongodb.com/cloud/atlas
- Criar uma REST API usando Django com as melhores práticas de desenvolvimento
- Integrar a API com o banco de dados MongoDB criado no Atlas para persistir os dados
- Recomendável usar (PyMongo)[https://api.mongodb.com/python/current/] 
- Desenvolver Testes Unitários

### Modelo de Dados:

Para a definição do modelo, consultar o arquivo [products.json](./products.json) que foi exportado do Open Food Facts. 

### Importar Dados:

Antes de seguir com o desafio, devemos exportar uma lista de produtos da base do Open Food Facts: (Open Food Desafio)[https://br.openfoodfacts.org/cgi/search.pl?action=process&sort_by=unique_scans_n&page_size=500&axis_x=energy-kj&axis_y=products_n&action=display]

Escolher o formato que seja mais cômodo para criar um script que importará todos os dados ao mongo, o Open Food tem os seguintes formatos:

- XSLX
- CSV

Nesse passo o importante é desenvolver um código que consiga processar o arquivo e subir toda a informação no banco de datos para realizar futuros testes dos endpoints da REST API.


### A REST API

Na REST API teremos um CRUD com os seguintes endpoints:

 - `GET /`: Detalhes da API, se conexão leitura e escritura com a base de datos está OK, horário da última vez que o CRON foi executado, tempo online e uso de memória.
 - `PUT /products/:code`: Será responsável por receber atualizações do Projeto Web
 - `DELETE /products/:code`: Mudar o status do produto para `trash`
 - `GET /products/:code`: Obter a informação somente de um produto da base de dados
 - `GET /products`: Listar todos os produtos da base de dados, adicionar sistema de paginação para não sobrecarregar o `REQUEST`.

Ao terminar os endpoints, configurar os testes usando Pytest.


## [Bônus] DevOps

Depois de um árduo trabalho de desenvolvimento na API chegou a hora mais esperada, 
o lançamento do projeto, é uma das partes mais motivadoras verdade? Então, a equipe de administração de 
sistemas precisará dos mínimos detalhes para configurar o projeto em produção, 
por isso é sua responsabilidade documentar todo o fluxo e facilitar a configuração dos dois projetos com 
tecnologias chaves para rodar em ambientes de Cloud Computing. 

Para isso deveremos configurar:

- Dockerfile
- Docker compose para executar o projeto em ambiente local


## Readme do Repositório
 
- Deve conter o título de cada projeto
- Uma descrição de uma frase
- Como instalar e usar o projeto (instruções)
