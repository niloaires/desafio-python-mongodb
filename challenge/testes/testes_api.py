from django.test import TestCase
from django.utils.crypto import get_random_string
import json
#Faker para criação de produtos
from faker import Faker
from faker_food import FoodProvider
fake=Faker()
fake.add_provider(FoodProvider)
from core.models import ProdutosModel

class ApiTeste(TestCase):

    def setUp(self):
        self.item=ProdutosModel.objects.create(code=get_random_string(length=5),
                                               product_name=fake.dish(),
                                               ingredients_text= fake.ingredient()
                                               )



    def teste_get_code(self):
        response=self.client.get('/api/products/{}'.format(self.item.code))
        retorno=json.loads(response.content)
        self.assertEqual(self.item.code, retorno['code'])

