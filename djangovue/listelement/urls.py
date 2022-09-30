from django.urls import path
from rest_framework import routers
from .viewsets import ElementViewSet, CategoryViewSet, TypeViewSet


route = routers.SimpleRouter()
route.register('element', ElementViewSet)
route.register('type', TypeViewSet)
route.register('category', CategoryViewSet)

urlpatterns = route.urls