from rest_framework.generics import CreateAPIView
from apps.product.models import Product
from apps.product.serializer import ProductSerializer

class ProductCreateAPIView(CreateAPIView):
    queryset = Product
    serializer_class = ProductSerializer
    
    