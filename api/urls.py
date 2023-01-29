from django.urls import path
from api.views import *
urlpatterns = [
    path('',ApiViewSet.as_view()),
    path('products', ProdutosViewSet.as_view({'get':'list', 'post':'create'})),
    path('products/<slug:code>', ProdutosViewSet.as_view(
        {

            'delete':'destroy',
            'get': 'retrieve',
            'put':'update'
         }), name='api_detalhar_produto'),
]