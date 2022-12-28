from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Element,Category,Type
from .serializer import ElementSerializer,CategorySerializer,TypeSerializer,CommentSerializer

from comment.models import Comment

class ElementViewSet(viewsets.ModelViewSet):
    serializer_class = ElementSerializer
    queryset = Element.objects.all()
    #Con el siguiente metodo si ponemos elements/all nos saca todos los elementos sin paginaciones
    @action(detail=False, methods=['get'])
    def all(self, request):
        queryset = Element.objects.all()
        serializer = ElementSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def url(self, request):
        #print("url limpia: "+request.query_params['url_clean'])
        #queryset = Element.objects.get(url_clean=request.query_params['url_clean'])
        queryset = get_object_or_404(Element,url_clean=request.query_params['url_clean'])
        serializer = ElementSerializer(queryset, many=False)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    @action(detail=True, methods=['get'])
    def elements(self, request, pk=None):
        queryset = Element.objects.filter(category_id=pk)
        serializer = ElementSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def all(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def url(self, request):
        #print("url limpia: "+request.query_params['url_clean'])
        #queryset = Element.objects.get(url_clean=request.query_params['url_clean'])
        queryset = get_object_or_404(Category,url_clean=request.query_params['url_clean'])
        serializer = CategorySerializer(queryset, many=False)
        return Response(serializer.data)

class TypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
    @action(detail=True, methods=['get'])
    def elements(self, request, pk=None):
        queryset = Element.objects.filter(type_id=pk)
        serializer = ElementSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def all(self, request):
        queryset = Type.objects.all()
        serializer = TypeSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def url(self, request):
        #print("url limpia: "+request.query_params['url_clean'])
        #queryset = Element.objects.get(url_clean=request.query_params['url_clean'])
        queryset = get_object_or_404(Type,url_clean=request.query_params['url_clean'])
        serializer = TypeSerializer(queryset, many=False)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.exclude(element__isnull=True) #no muestra ningun comentario que no esté asociado a un elemento
    #queryset = Comment.objects.all()
    @action(detail=False, methods=['get'])
    def all(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)
    