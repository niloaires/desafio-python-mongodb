import os
import csv
import pymongo
from decouple import config
from rest_framework import status
from rest_framework.response import Response
from django.core.files.storage import default_storage
from core.models import ProdutosModel


class Importacao:
    def __init__(self, file):
        self.file = file
        self.fields_modelo = ['code', 'lc', 'status', 'product_name', 'quantity',
                              'brands', 'categories', 'labels', 'cities',
                              'purchase_places', 'stores', 'ingredients_text',
                              'url', 'creator', 'traces', 'serving_quantity', 'serving_size', 'nutriscore_score',
                              'nutriscore_grade', 'main_category', 'image_url', 'imported_t', 'created_t',
                              'last_modified_t']

    def send_csv(self):
        if not self.__check_file_format():
            content = {'Formato de file não suportado': 'Envie um file no formato CSV'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        file = default_storage.save(self.file.name, self.file)
        file = default_storage.open(file)
        json_array = []
        with open(file.file.name, 'r', encoding='utf-8') as f:
            read_csv = csv.DictReader(f, dialect='excel', delimiter='\t')
            for item in read_csv:
                line = {}
                for field in read_csv.fieldnames:
                    line[field] = item[field]
                json_array.append(line)
        total = len(json_array)
        self.__refact_list(original_list=json_array)

        return total

    def __check_file_format(self):
        ext = os.path.splitext(self.file.file.name)[-1].lower()
        if ext == '.csv':
            return True
        else:
            return False

    def __refact_list(self, original_list):
        new_list = []
        check_last_register = ProdutosModel.objects.all().count()
        for item in original_list:
            check_last_register += 1
            new_dictionary = dict()
            for (key, value) in item.items():
                local = item['lc']
                code = item['code']
                if item['lc'] is not None:
                    if item.get("product_name_{local}".format(local=local)):
                        new_dictionary['product_name'] = item["product_name_{local}".format(local=local)]
                    if item.get("ingredients_text_{local}".format(local=local)):
                        new_dictionary['ingredients_text'] = item[
                            "ingredients_text_{local}".format(local=local)]
                if key in self.fields_modelo:
                    new_dictionary[key] = value
                new_dictionary['id'] = check_last_register
            new_list.append(new_dictionary)
        if new_list:
            self.__commit_list(refactored_list=new_list)
        else:
            raise RuntimeError

    def __commit_list(self, refactored_list):
        client = pymongo.MongoClient(config('ATLAS_CONEXAO'))
        db = client['challenge']
        col = db['core_produtosmodel']
        col.insert_many(refactored_list)
        client.close()
