from django.test import TestCase
from core.models import ProdutosModel
class ProdutosTesteCase(TestCase):

    def setUp(self):
        self.item=ProdutosModel.objects.create(code='1243454', product_name='Produto 01', brands='Marca')

    def test_return_str(self):

        self.assertEqual(self.item.__str__(), str("{} - {}".format(self.item.product_name, self.item.brands)))

    def teste_link_detalhes_api(self):

        url=str('/products/{}'.format(self.item.code))
        self.assertEqual(url, self.item.url_api())
