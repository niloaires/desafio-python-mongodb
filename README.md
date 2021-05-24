# Python Challenge 20200205

## Introdução

Nesse desafio trabalharemos no desenvolvimento de uma REST API para utilizar os dados do projeto Open Food Facts, que é um banco de dados aberto com informação nutricional de diversos produtos alimentícios.

O projeto tem como objetivo dar suporte a equipe de nutricionistas da empresa Fitness Foods LC para que eles possam revisar de maneira rápida a informação nutricional dos alimentos que os usuários enviam pela aplicação móvel.

### Obrigatório
 
- Trabalhar em um FORK deste repositório em seu usuário;
- O projeto back-end deverá ser desenvolvido usando Python utilizando um dos frameworks: [Django Rest Framework](https://www.django-rest-framework.org) ou [Flask](https://flask.palletsprojects.com/en/1.1.x/);
- Configurar os testes usando Pytest ou algum de sua preferência;
- Documentação para configuração do projeto em ambientes de produção (instalações, executar, referências e etc);
 

## O projeto
 
- Criar um banco de dados MongoDB usando Atlas: https://www.mongodb.com/cloud/atlas ou algum Banco de Dados SQL se não sentir confortável com NoSQL;
- Criar uma REST API usando Django Rest Framework com as melhores práticas de desenvolvimento
- Integrar a API com o banco de dados criado para persistir os dados
- Recomendável usar Drivers oficiais para integração com o DB
- Desenvolver Testes Unitários

### Modelo de Dados:

Para a definição do modelo, consultar o arquivo [products.json](./products.json) que foi exportado do Open Food Facts. 

### Importar Dados:

Antes de seguir com o desafio, devemos exportar uma lista de produtos da base do Open Food Facts: [Open Food Desafio](https://br.openfoodfacts.org/cgi/search.pl?action=process&sort_by=unique_scans_n&page_size=500&axis_x=energy-kj&axis_y=products_n&action=display)

Escolher o formato que seja mais cômodo para criar um script que importará todos os dados ao mongo, o Open Food tem os seguintes formatos:

- XLSX
- CSV

Nesse passo o importante é desenvolver um código que consiga processar o arquivo e subir toda a informação no banco de dados para realizar futuros testes dos endpoints da REST API.


### A REST API

Na REST API teremos um CRUD com os seguintes endpoints:

 - `GET /`: Detalhes da API, se conexão leitura e escritura com a base de dados está OK, horário da última vez que o CRON foi executado, tempo online e uso de memória.
 - `PUT /products/:code`: Será responsável por receber atualizações do Projeto Web
 - `DELETE /products/:code`: Mudar o status do produto para `trash`
 - `GET /products/:code`: Obter a informação somente de um produto da base de dados
 - `GET /products`: Listar todos os produtos da base de dados, adicionar sistema de paginação para não sobrecarregar o `REQUEST`.


### Extras

- **Diferencial 1** Escrever Unit Test para os endpoints da REST API
- **Diferencial 2** Executar o projeto usando Docker
- **Diferencial 3** Escrever um esquema de segurança utilizando `API KEY` nos endpoints. Ref: https://learning.postman.com/docs/sending-requests/authorization/#api-key
- **Diferencial 4** Descrever a documentação da API utilizando o conceito de Open API 3.0;


## Readme do Repositório
 
- Deve conter o título de cada projeto
- Uma descrição de uma frase
- Como instalar e usar o projeto (instruções)
- Não esqueça o [.gitignore](https://www.toptal.com/developers/gitignore)
 
## Finalização 

Avisar sobre a finalização e enviar para correção em: [https://coodesh.com/review-challenge](https://coodesh.com/review-challenge) 
Após essa etapa será marcado a apresentação/correção do projeto.

## Instruções para a Apresentação: 

1. Será necessário compartilhar a tela durante a vídeo chamada;
2. Deixe todos os projetos de solução previamente abertos em seu computador antes de iniciar a chamada;
3. Deixe os ambientes configurados e prontos para rodar; 
4. Prepara-se pois você será questionado sobre cada etapa e decisão do Challenge;
5. Prepare uma lista de perguntas, dúvidas, sugestões de melhorias e feedbacks (caso tenha).


## Suporte

Use o nosso canal no slack: http://bit.ly/32CuOMy para tirar dúvidas sobre o processo ou envie um e-mail para contato@coodesh.com. 
