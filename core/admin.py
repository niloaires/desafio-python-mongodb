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
    arquivo=forms.FileField(label='Arquivo', help_text='Atenção, apenas arquivo no formato .csv',
                               validators=[FileExtensionValidator(['csv'])])



class ProdutosAdmin(admin.ModelAdmin):

    list_display = ['product_name', 'code']
    list_filter = ['status',]
    def get_urls(self):
        urls = super().get_urls()
        nova_urls=[path('carregar_csv', self.carregar_arquivo, name='carregar_csv')]
        return urls+nova_urls


    @transaction.atomic()
    def carregar_arquivo(self, request):
        if request.method=='POST':
            formulario=FormUpload(request.POST, request.FILES)
            if formulario.is_valid():
                arquivoForm=request.FILES['arquivo']
                arquivoForm_nome=default_storage.save(arquivoForm.name, arquivoForm)
                jsonArray = []
                arquivo=default_storage.open(arquivoForm_nome)
                campos_modelo=['code', 'status', 'product_name', 'quantity',
                        'brands', 'categories', 'labels', 'cities',
                        'purchase_places', 'stores', 'ingredients_text',
                        'url', 'creator', 'traces', 'serving_quantity', 'serving_size', 'nutriscore_score',
                        'nutriscore_grade', 'main_category', 'image_url', 'imported_t', 'created_t',
                        'last_modified_t']
                t=[]
                bulk_lista=[]
                objs = []
                with open(arquivo.file.name, 'r', encoding="utf8") as f:
                    dictRangObject=csv.DictReader(f, dialect='excel', delimiter='\t')

                    for item in dictRangObject:
                        #Para cada item do CSV, o código abrirá um Dicionário
                        linha = {}
                        #O Dicionário é preenchido com o título do campo e o seu respectivo valor
                        for campo in dictRangObject.fieldnames:
                            linha[campo]=item[campo]
                        """
                        Após inserir todos os dados no dicionário, cria-se uma lista de dicionários 
                        """
                        t.append(linha)
                        """
                        Tendo como base o arquivo CSV emitido pelo sítio https://br.openfoodfacts.org, observei que
                        há uma variação no título do campo, com base em um outro campo, identificado pro 'lc'
                        dessa forma, campos como product_name variam de acordo com o 'lc', podendo ser por exemplo
                        produtc_name_lc. Outra singularidade, é o fato de vários campos do CSV não estão mencionados nos 
                        requisitos do  Modelo solicitado neste desafio.
                        Para tratar essas partiularidades:
                        1-Abro um novo dicionário para cada linha, comparando o título da chave com a lista de campos do
                        modelo
                        """
                        novoDicionario = dict()
                        for (k, v) in linha.items():
                            local = linha['lc']
                            if linha['lc'] is not None:
                                if linha.get(str("product_name_{local}".format(local=local))):
                                    novoDicionario['product_name'] = linha[str("product_name_{local}".format(local=local))]
                                if linha.get(str("ingredients_text_{local}".format(local=local))):
                                    novoDicionario['ingredients_text'] = linha[
                                        str("ingredients_text_{local}".format(local=local))]
                                    # Provendo a garantia de que mesmo que não haja dados, o looping continuará

                            if k in campos_modelo:
                                novoDicionario[k] = v

                        bulk_lista.append(novoDicionario)
                    #Iniciar preparação para registro no Banco de Dados

                    for item in bulk_lista[0:500]:
                        for itemCampoModelo in campos_modelo:
                            if itemCampoModelo not in item.keys():
                                item[itemCampoModelo]=None
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
                messages.add_message(request, messages.SUCCESS, 'O arquivo Csv foi processado')
                return HttpResponseRedirect(request.get_full_path())

            else:
                contexto={
                    'formulario':formulario
                }
                return render(request, "admin/core/produtosmodel/carregar_arquivo.html", contexto)
        contexto={
            'formulario':FormUpload
        }
        return render(request, "admin/core/produtosmodel/carregar_arquivo.html", contexto)


admin.site.register(ProdutosModel, ProdutosAdmin)