import os
from django.test import TestCase
from django.utils.crypto import get_random_string
import json
from faker import Faker
from faker_food import FoodProvider
from core.models import ProdutosModel
from django.core.files.storage import default_storage
from pathlib import Path

fake = Faker()
fake.add_provider(FoodProvider)
BASE_DIR = Path(__file__).resolve().parent.parent


class ApiTeste(TestCase):

    def setUp(self):
        self.file = os.path.join(BASE_DIR, '../media/exemplo.csv')
        self.item = ProdutosModel.objects.create(code=get_random_string(length=5),
                                                 product_name=fake.dish(),
                                                 ingredients_text=fake.ingredient()
                                                 )

    def teste_get_code(self):
        code = self.item.code
        request = self.client.get('/api/products/{}'.format(code))
        retorno = json.loads(request.content)
        self.assertEqual(self.item.code, retorno['code'])

    def teste_post_csv(self):
        file = default_storage.open(self.file)
        ext = os.path.splitext(file.name)[-1].lower()
        self.assertEqual(ext, '.csv')

    def teste_delete(self):
        code = self.item.code
        request = self.client.delete('/api/products/{}'.format(code))
        self.assertEqual(request.status_code, 200)

    def teste__check_inicial(self):
        request = self.client.get('/api/')
        self.assertEqual(request.status_code, 200)
