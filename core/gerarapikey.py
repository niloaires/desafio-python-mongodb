from rest_framework_api_key.models import APIKey

class gerarchave:
    def __init__(self, nome):
        self.nome=nome
    def gerar(self):
        api_key, key = APIKey.objects.create_key(name=self.nome)
        return api_key.get_fromkey()

