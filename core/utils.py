import os
import csv
import json
import pymongo
from decouple import config
from rest_framework import status
from rest_framework.response import Response
from django.core.files.storage import default_storage
from core.models import ProdutosModel
class Importacao:
    def __init__(self, arquivo):
        self.arquivo=arquivo
        self.campos_modelo = ['code', 'lc', 'status', 'product_name', 'quantity',
                     'brands', 'categories', 'labels', 'cities',
                     'purchase_places', 'stores', 'ingredients_text',
                     'url', 'creator', 'traces', 'serving_quantity', 'serving_size', 'nutriscore_score',
                     'nutriscore_grade', 'main_category', 'image_url', 'imported_t', 'created_t',
                     'last_modified_t']


    def remeterCsv(self):
        if not self.__verificarFormatoArquivo():
            content = {'Formato de arquivo não suportado': 'Envie um arquivo no formato CSV'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        arquivo = default_storage.save(self.arquivo.name, self.arquivo)
        arquivo=default_storage.open(arquivo)
        jsonArray=[]
        with open(arquivo.file.name, 'r', encoding='utf-8') as f:
            lerCsv = csv.DictReader(f, dialect='excel', delimiter='\t')
            for item in lerCsv:
                linha={}
                for campo in lerCsv.fieldnames:
                    linha[campo]=item[campo]
                jsonArray.append(linha)
        total=len(jsonArray)
        self.__refatorarLista(listaOriginal=jsonArray)

        return total
    def __verificarFormatoArquivo(self):
        extensao = os.path.splitext(self.arquivo.file.name)[-1].lower()
        if extensao == '.csv':
            return True
        else:
            return False
    def __refatorarLista(self, listaOriginal):
        novaLista=[]
        checarUltimoRegistro=ProdutosModel.objects.all().count()
        for item in listaOriginal:
            checarUltimoRegistro+=1
            novoDicionario = dict()
            for (chave,valor) in item.items():
                local=item['lc']
                code=item['code']
                if item['lc'] is not None:
                    if item.get(str("product_name_{local}".format(local=local))):
                        novoDicionario['product_name'] = item[str("product_name_{local}".format(local=local))]
                    if item.get(str("ingredients_text_{local}".format(local=local))):
                        novoDicionario['ingredients_text'] = item[
                            str("ingredients_text_{local}".format(local=local))]
                if chave in self.campos_modelo:
                    novoDicionario[chave]=valor
                novoDicionario['id']=checarUltimoRegistro
            novaLista.append(novoDicionario)
        if novaLista:
            self.__subirLista(listaRefatorada=novaLista)
        else:
            raise RuntimeError


    def __subirLista(self, listaRefatorada):
        client = pymongo.MongoClient(config('ATLAS_CONEXAO'))
        db = client['challenge']
        col = db['core_produtosmodel']
        col.insert_many(listaRefatorada)
        client.close()



