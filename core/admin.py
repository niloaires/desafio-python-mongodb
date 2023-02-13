from django.contrib import admin
from django.urls import path
from django.db import transaction
from django.shortcuts import render, redirect
from core.models import ProdutosModel
from django import forms

from django.core.validators import FileExtensionValidator
from django.core.files.storage import default_storage
from django.http import JsonResponse, HttpResponseRedirect
import csv
from django.contrib import messages


# Register your models here.

class FormUpload(forms.Form):
    file = forms.FileField(label='file', help_text='Atenção, apenas file no formato .csv',
                           validators=[FileExtensionValidator(['csv'])])


class ProdutosAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'code']
    list_filter = ['status', ]

    def get_urls(self):
        urls = super().get_urls()
        nova_urls = [path('carregar_csv', self.carregar_file, name='carregar_csv')]
        return urls + nova_urls

    @transaction.atomic()
    def carregar_file(self, request):
        if request.method == 'POST':
            formulario = FormUpload(request.POST, request.FILES)
            if formulario.is_valid():
                file_form = request.FILES['file']
                file_form_nome = default_storage.save(file_form.name, file_form)
                json_array = []
                file = default_storage.open(file_form_nome)
                fields_modelo = ['code', 'status', 'product_name', 'quantity',
                                 'brands', 'categories', 'labels', 'cities',
                                 'purchase_places', 'stores', 'ingredients_text',
                                 'url', 'creator', 'traces', 'serving_quantity', 'serving_size', 'nutriscore_score',
                                 'nutriscore_grade', 'main_category', 'image_url', 'imported_t', 'created_t',
                                 'last_modified_t']
                t = []
                bulk_lista = []
                objs = []
                with open(file.file.name, 'r', encoding="utf8") as f:
                    dict_ragne_object = csv.DictReader(f, dialect='excel', delimiter='\t')

                    for item in dict_ragne_object:
                        # Para cada item do CSV, o código abrirá um Dicionário
                        line = {}
                        # O Dicionário é preenchido com o título do field e o seu respectivo valor
                        for field in dict_ragne_object.fieldnames:
                            line[field] = item[field]
                        """
                        Após inserir todos os dados no dicionário, cria-se uma lista de dicionários 
                        """
                        t.append(line)
                        """
                        Tendo como base o file CSV emitido pelo sítio https://br.openfoodfacts.org, observei que
                        há uma variação no título do field, com base em um outro field, identificado pro 'lc'
                        dessa forma, fields como product_name variam de acordo com o 'lc', podendo ser por exemplo
                        produtc_name_lc. Outra singularidade, é o fato de vários fields do CSV não estão mencionados nos 
                        requisitos do  Modelo solicitado neste desafio.
                        Para tratar essas partiularidades:
                        1-Abro um novo dicionário para cada line, comparando o título da chave com a lista de fields do
                        modelo
                        """
                        new_dict = dict()
                        for (k, v) in line.items():
                            local = line['lc']
                            if line['lc'] is not None:
                                if line.get("product_name_{local}".format(local=local)):
                                    new_dict['product_name'] = line["product_name_{local}".format(local=local)]
                                if line.get("ingredients_text_{local}".format(local=local)):
                                    new_dict['ingredients_text'] = line[
                                        "ingredients_text_{local}".format(local=local)]
                                    # Provendo a garantia de que mesmo que não haja dados, o looping continuará

                            if k in fields_modelo:
                                new_dict[k] = v

                        bulk_lista.append(new_dict)
                    # Iniciar preparação para registro no Banco de Dados

                    for item in bulk_lista[0:500]:
                        for itemfieldModelo in fields_modelo:
                            if itemfieldModelo not in item.keys():
                                item[itemfieldModelo] = None
                        objs.append(ProdutosModel(
                            code=item['code'],
                            status=item['status'],
                            product_name=item['product_name'],
                            quantity=item['quantity'],
                            brands=item['brands'],
                            categories=item['categories'],
                            labels=item['labels'],
                            cities=item['cities'],
                            purchase_places=item['purchase_places'],
                            stores=item['stores'],
                            ingredients_text=item['ingredients_text'],
                            url=item['url'],
                            creator=item['creator'],
                            traces=item['traces'],
                            serving_size=item['serving_size'],
                            serving_quantity=item['serving_quantity'],
                            nutriscore_score=item['nutriscore_score'],
                            nutriscore_grade=item['nutriscore_grade'],
                            image_url=item['image_url'],
                            created_t=item['created_t'],
                            last_modified_t=item['last_modified_t']
                        ))
                    ProdutosModel.objects.bulk_create(objs)
                messages.add_message(request, messages.SUCCESS, 'O file Csv foi processado')
                return HttpResponseRedirect(request.get_full_path())

            else:
                contexto = {
                    'formulario': formulario
                }
                return render(request, "admin/core/produtosmodel/carregar_file.html", contexto)
        contexto = {
            'formulario': FormUpload
        }
        return render(request, "admin/core/produtosmodel/carregar_file.html", contexto)


admin.site.register(ProdutosModel, ProdutosAdmin)
