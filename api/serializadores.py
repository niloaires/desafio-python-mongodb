from rest_framework import serializers
from core.models import ProdutosModel

class ProdutosSerializer(serializers.ModelSerializer):
    code=serializers.CharField(read_only=True)
    detalhar = serializers.HyperlinkedIdentityField(view_name='api_detalhar_produto', lookup_field='code', format='html')
    class Meta:

        model = ProdutosModel
        fields = '__all__'
