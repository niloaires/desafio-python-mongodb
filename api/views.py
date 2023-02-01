from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from api.paginador import paginaCaoPersonalizada
from rest_framework.response import Response
from api.serializadores import ProdutosSerializer
from core.utils import Importacao
from core.models import ProdutosModel
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
import pymongo
import psutil
from decouple import config

# Create your views here.
class ApiViewSet(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        conexaoMongo=pymongo.MongoClient(config('ATLAS_CONEXAO'))

        try:
            conexaoMongo.server_info()
            bancoDisponivel=True
            leituraDisponivel=True
            db=conexaoMongo['challenge']
            if db['teste']:
                escritaDisponivel=True
                db['teste'].drop()
            else:
                escritaDisponivel=False

        except:
            bancoDisponivel=False
            leituraDisponivel = False
            escritaDisponivel=False

        #Memória
        usoCPU=str("{} %".format(psutil.cpu_percent(4)))
        usoMemoria=psutil.virtual_memory()
        content={
            'Disponibilidade do banco':bancoDisponivel,
            'Autorização de Leitura':leituraDisponivel,
            'Autorização de Escrita':escritaDisponivel,
            'Percentual de uso da CPU:':usoCPU,
            'Uso da memória': str("{} %".format(usoMemoria.percent))

        }
        return Response(content)

class ProdutosViewSet(viewsets.ModelViewSet):
    serializer_class = ProdutosSerializer
    pagination_class = paginaCaoPersonalizada
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        arquivo=request.FILES['arquivo']
        enviarParaBanco=Importacao(arquivo)
        if enviarParaBanco:
            content = {'Dados enviados.'' {} registros foram enviados para o Banco de Dados'.format(
            enviarParaBanco.remeterCsv())}
            return Response(content, status=status.HTTP_200_OK)
        else:
            content={'Houve um problema com sua requisição':'Verifique seu arquivo'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return ProdutosModel.objects.exclude(status='trash').order_by('product_name')
    def get_object(self, *args, **kwargs):
        return get_object_or_404(ProdutosModel, code=self.kwargs.get("code"))
    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(ProdutosModel, code=self.kwargs.get("code"))
        instance.status="trash"
        instance.save()
        return Response({'success': 'O registro foi removido'}, status=status.HTTP_200_OK)
    def partial_update(self, request, *args, **kwargs):
        instance = get_object_or_404(ProdutosModel, code=self.kwargs.get("code"))
        serializer=ProdutosSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

