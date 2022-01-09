from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status
from .serializers import ProductDetailSerializer, ProductSerializer
from .models import Product
 

# Create your views here.
@api_view(["GET"])
def Product_list_view(request):
    products = Product.object.all()
    data = ProductSerializer(Product, many=True).data
    return Response(data=data)


@api_view(["GET"])
def Product_detail_view(request, id):
    try:
        products = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error':'Movie not found'})

    data = ProductDetailSerializer(Product, many=False).data
    return Response(data=data)