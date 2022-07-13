from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your tests here.
from .models import Product
from .serializers import ProductSerializer

class LatestProductsList(APIView):
  def get(self, request, format=None):
    products = Product.objects.all()[0:4]
    seralizer = ProductSerializer(products, many=True)
    return Response(seralizer.data)
