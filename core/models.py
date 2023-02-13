from django.db import models


# Create your models here.
class ProdutosModel(models.Model):
    code = models.CharField(max_length=20, verbose_name='Código', blank=False,
                            null=False, unique=True)
    status = models.CharField(max_length=10, verbose_name='Status', blank=False,
                              null=False, default='published')
    product_name = models.CharField(max_length=250, verbose_name='Nome do produto', blank=False,
                                    null=False, default='Título do produto desconhecido')
    quantity = models.CharField(max_length=200, verbose_name='Quantidade', blank=True,
                                null=False, default='Sem informações sobre quantidades')
    brands = models.CharField(max_length=100, verbose_name='Marcas', blank=True, null=False,
                              default='Sem informações sobre Marcas')
    categories = models.CharField(max_length=255, verbose_name='Categorias', blank=True,
                                  null=False, default='Sem informações sobre Categorias')
    labels = models.CharField(max_length=255, verbose_name='Labels', blank=True,
                              null=False, default='Sem informações sobre Labels')
    cities = models.CharField(max_length=255, verbose_name='Cidades', blank=True,
                              null=False, default='Sem informações sobre cidades')
    purchase_places = models.CharField(max_length=255, verbose_name='Locais de compra', blank=True,
                                       null=False, default='Sem informações sobre Locais de compra')
    stores = models.CharField(max_length=255, verbose_name='Lojas', blank=True,
                              null=False, default='Sem informações sobre lojas')
    ingredients_text = models.TextField(blank=True, null=False, default='Sem informações sobre ingredientes')
    url = models.CharField(max_length=255, verbose_name='Url', blank=True,
                           null=False, default='Não há uma URL registrada')
    creator = models.CharField(max_length=20, verbose_name='Criador', blank=True, null=False,
                               default='Não informado')
    traces = models.CharField(max_length=255, verbose_name='Traces', blank=True, null=False,
                              default='Sem informações sobre Traces')
    serving_size = models.CharField(max_length=50, verbose_name='Porçoes', blank=True, null=False,
                                    default='Sem informações sobre Porções')
    serving_quantity = models.CharField(max_length=50, verbose_name='Quantidade servida', blank=True, null=False,
                                        default=None)
    nutriscore_score = models.CharField(max_length=50, verbose_name='Nutriscore', blank=True, null=False,
                                        default=0)
    nutriscore_grade = models.CharField(max_length=5, verbose_name='Nota Nutriscore', blank=True, null=True)
    main_category = models.CharField(max_length=100, verbose_name='Categoria principal', blank=True, null=False,
                                     default='Sem informações sobre Categoria principal')
    image_url = models.CharField(max_length=255, verbose_name='Url da imagem', blank=True, null=False,
                                 default='Sem URL de imagem do Produto')
    imported_t = models.DateTimeField(auto_now=True, verbose_name='Data e hora da importação')
    created_t = models.DateField(blank=True, null=True, verbose_name='Data da criação')
    last_modified_t = models.DateField(blank=True, null=True, verbose_name='Data da última modificação')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return "{} - {}".format(self.product_name, self.brands)

    def url_api(self):
        return "/products/{}".format(self.code)
