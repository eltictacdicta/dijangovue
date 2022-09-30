from rest_framework import viewsets

from .models import Element,Category,Type
from .serializer import ElementSerializer,CategorySerializer,TypeSerializer

class ElementViewSet(viewsets.ModelViewSet):
    serializer_class = ElementSerializer
    queryset = Element.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TypeViewSet(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
    