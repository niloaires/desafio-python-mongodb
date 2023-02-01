# API Rest - Open food facts by Nilo Aires Jr.

Aplicação em Python / django rest_framework que captura dados de um arquivo .cvs e os insere na base de dados, observando o modelo exigido, disponibilizando uma API REST para consumo de dados.

​

### Configuração

* Clone este repositório

* Em uma máquina com o Python 3 crie um ambiente virtual

* Instale as dependências

* Inicie o servidor

​

```

git clone https://lab.coodesh.com/nilo_aires/python-challenge-20200205.git

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python manage.py runserver

```

Esta ação deverá iniciar o servidor na porta **8000**.

##Recursosos  disponíveis

​

```

GET /api/ (Exibe o status da API)

POST /api/products (Remete arquivo no formato .csv para o Banco de Dados)

GET /api/products (Lista todos os produtos com o status diferente de 'trash', paginados de 10 em 10)

GET /api/products/:code (Retorna detalhes do produto com base no campo 'code')

PUT /api/products/:code (Atualiza atributos do produto com base no campo 'code')

DELETE /api/products/:code (Altera o atributo status para 'trash')

```

​

#### [GET /api/]

Apresenta informações referentes ao Status da API, disponibilidade, conexão com a base de dados e outros aspectos.

​

#### [POST /api/products/]

Recebe um arquivo no fortato **.csv**, converte cada linha em um novo objeto, avaliando o campo 'lc' do arquivo para definir sua localidade e definir o nome do produto (quando houver), por fim, alimenta a base de dados, respeitando o atributo code dos registros já existentes.

​

#### [GET /api/products/]

Recupera a lista de objetos com o atrituto status diferente de 'trash' existentes na base de dados, paginando-os de 10 em 10 para evitar sobrecarga na requisição.

#### [GET /api/products/:code]

Recupera os dados de um produto específico, identificado por seu atributo `code`



##### Ultimas considerações

Com exceção do endpoit /, os demais exigem o uso de Token no header Authorization
Example
